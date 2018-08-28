"""Base model setup for sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, ForeignKey, Column, Integer

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

association_table = Table('association', Base.metadata, Column('user_id', Integer, ForeignKey('user.id')),
                          Column('menu_id', Integer, ForeignKey('menu.id')))
