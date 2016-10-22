import os
from missing_license import app
from missing_license import init_db

if __name__ == "__main__":
    init_db()
    app.run(host=app.config['IP'], port=app.config['PORT'])

application = app
