"""User Model"""
from data.base import Base, association_table
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe")
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="menus")
