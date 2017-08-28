from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
from app import models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os.path
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	api.create(SQLALCHEMY_MIGRATE_REPO, 'database_repository')
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(SQLALCHEMY_DATABASE_URI,
		SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))