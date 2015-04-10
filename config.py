import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

WTF_CSRF_ENABLED = True
CSRF_SESSION_KEY = "oemah"
SECRET_KEY = 'oemah'

#user request api
USERNAME = 'oemah'
PASWD = 'admin1234'
