from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, TIMESTAMP
from datetime import datetime;

#
db = SQLAlchemy()


class BaseModel(object):
    """ Base model which include common column in all models """
    id = Column(Integer, primary_key=True)
    created_ts = Column(TIMESTAMP(), default=datetime.now())
    updated_ts = Column(TIMESTAMP(), default=datetime.now(), onupdate=datetime.now())