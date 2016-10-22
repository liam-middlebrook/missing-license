import os

from flask import Flask
from flask_github import GitHub
from flask_github import GitHubError

import requests

from flask import Flask
from flask import request
from flask import g
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask.ext.github import GitHub

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


issue_body = """
First, the standard disclaimer: I am not a lawyer, and this does not constitute legal or financial advice.

Generally, IMHO, it is a good idea to use FSF or OSI Approved Licenses (which can be found here https://www.gnu.org/licenses/licenses.html and here http://opensource.org/licenses/category)

The Free Software Foundation has a useful guide for choosing a license: https://www.gnu.org/licenses/license-recommendations.html

I often reference the Software Freedom Law Center's Legal Primer for both practical and academic purposes (highly recommended): https://www.softwarefreedom.org/resources/2008/foss-primer.html#x1-60002.2

https://tldrlegal.com/ is quite a useful resource for comparing the various FOSS licenses out there once you have some context

To get ahold of actual lawyers/advisors who help FOSS projects, you can reach out to the FSF, SFLC, and OSI at:
licensing@fsf.org
help@softwarefreedom.org
license-discuss@opensource.org

Hope this helps, and happy hacking!
"""

app = Flask(__name__)

if os.path.exists(os.path.join(os.getcwd(), "config.py")):
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.py"))
else:
    app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

# Disable SSL certificate verification warning
requests.packages.urllib3.disable_warnings()

github = GitHub(app)

# setup sqlalchemy
engine = create_engine('sqlite:////tmp/github-flask.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    github_access_token = Column(String(200))

    def __init__(self, github_access_token):
        self.github_access_token = github_access_token


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@app.after_request
def after_request(response):
    db_session.remove()
    return response

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

@app.route('/')
def index():
    status = request.args.get('status')
    return render_template("index.html",
                           logged_in=g.user,
                           status=status)

@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token


@app.route('/github-callback')
@github.authorized_handler
def authorized(access_token):
    next_url = request.args.get('next') or url_for('index')
    if access_token is None:
        return redirect(next_url)

    user = User.query.filter_by(github_access_token=access_token).first()
    if user is None:
        user = User(access_token)
        db_session.add(user)
    user.github_access_token = access_token
    db_session.commit()

    session['user_id'] = user.id
    return redirect(next_url)


@app.route('/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize(scope="public_repo")
    else:
        return 'Already logged in'


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/file', methods=['POST'])
def file_issue():
    data = \
    {
        'title': "Missing License!?",
        'body': issue_body
    }

    username = request.form.get('username')
    repo = request.form.get('repository')

    try:
        github.get('repos/' + username + '/' + repo)
    except GitHubError:
        return redirect('/?status=bad')

    github.post('repos/' + username + '/' + repo + '/issues', data)
    return redirect('/?status=ok')
