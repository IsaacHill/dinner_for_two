"""Module for the Menu db schema"""
from data.base import Base, association_table, db_session
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship


class Menu(Base):
    """Menu SQLAlchemy Model"""
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe")
    created = Column(DateTime, default=func.now())
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="menus")

    def save_to_db(self):
        """Save the menu to the database"""
        db_session.add(self)
        db_session.commit()
