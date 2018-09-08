"""Module for the Recipe db table and SQLAlchemy Model"""

from data.base import Base, db_session
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class Recipe(Base):
    """Recipe model for db"""
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_on = Column(DateTime, default=func.now())
    menu_id = Column(Integer, ForeignKey('menu.id'))
    method = Column(Text)
    time = Column(Text)
    serves = Column(Integer)
    equipment = Column(Text)
    comments = Column(Text)
    ingredients = relationship("Ingredient")

    def save_to_db(self):
        """Saves the recipe to the db"""
        db_session.add(self)
        db_session.commit()
