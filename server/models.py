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

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('menu_id', Integer, ForeignKey('menu.id'))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(50), unique = True, nullable= False)
    menus = relationship(
        "Menu",
        secondary=association_table,
        back_populates="users")



class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe")
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="menus")


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_on = Column(DateTime, default=func.now())
    menu_id = Column(Integer, ForeignKey('menu.id'))
    method = Column(Text)
    ingredients = relationship("Ingredient")
    serves = Column(Integer)

class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    quantity = Column(Float)
    recipie_id = Column(Integer, ForeignKey('recipe.id'))
    unit = Column(String)
    