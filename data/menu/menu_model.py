"""User Model"""
from data.base import Base, association_table, db_session
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipes = relationship("Recipe")
    created = Column(Date)
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="menus")

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()
