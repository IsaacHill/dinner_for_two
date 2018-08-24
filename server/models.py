# flask_sqlalchemy/models.py
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()

# association_table = Table('association', Base.metadata,
#     Column('left_id', Integer, ForeignKey('left.id')),
#     Column('right_id', Integer, ForeignKey('right.id'))
# )

# class User(Base):
#     __tablename__ = 'left'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String(50), unique = True, nullable= False)
#     menus = relationship(
#         "Menu",
#         secondary=association_table,
#         back_populates="users")



class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe")


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_on = Column(DateTime, default=func.now())
    menu_id = Column(Integer, ForeignKey('menu.id'))