"""Module for the Recipe db table and SQLAlchemy Model"""

from data.base import Base, db_session
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class Recipe(Base):
    """Recipe model for db"""
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    name = Column(String)
    created_on = Column(DateTime, default=func.now())
    method = Column(Text)
    time = Column(Text)
    serves = Column(Integer)
    equipment = Column(Text)
    comments = Column(Text)
    ingredients = relationship("Ingredient")

    @classmethod
    def recipe_by_id(cls, recipe_id):
        """Returns recipe with the matching id"""
        return cls.query.filter_by(id=recipe_id).first()

    def save_to_db(self):
        """Saves the recipe to the db"""
        db_session.add(self)
        db_session.commit()

    def remove_from_db(self):
        """Remove this recipe from the db"""
        db_session.delete(self)
        db_session.commit()
