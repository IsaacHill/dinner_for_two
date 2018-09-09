"""User Model"""
from data.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    name = Column(String, index=True)
    quantity = Column(Float)
    unit = Column(String)