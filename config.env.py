import os

# Flask config
DEBUG=False
IP=os.environ.get('MISSING_LICENSE_IP', '0.0.0.0')
PORT=os.environ.get('MISSING_LICENSE_PORT', '8080')
SERVER_NAME = os.environ.get('MISSING_LICENSE_SERVER_NAME', 'missing-license.csh.rit.edu')
SECRET_KEY = os.environ.get('MISSING_LICENSE_SECRET_KEY', '')

GITHUB_CLIENT_ID = os.environ.get('MISSING_LICENSE_GITHUB_CLIENT_ID','')
GITHUB_CLIENT_SECRET = os.environ.get('MISSING_LICENSE_GITHUB_CLIENT_SECRET','')
