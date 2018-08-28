"""Recipe model"""

from data.base import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_on = Column(DateTime, default=func.now())
    menu_id = Column(Integer, ForeignKey('menu.id'))
    method = Column(Text)
    ingredients = relationship("Ingredient")
    serves = Column(Integer)