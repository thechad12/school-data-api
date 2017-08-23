import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://kevin:George06820@localhost/edu'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')