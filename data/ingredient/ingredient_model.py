"""User Model"""
from data.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    quantity = Column(Float)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    unit = Column(String)