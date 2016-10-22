import sys

from flask import Flask
from flask.ext.github import GitHub

import requests


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

@app.route("/")
def index():
    return "Hello World!"
