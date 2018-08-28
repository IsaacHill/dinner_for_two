"""User Model"""
from data.base import Base, association_table
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(50), unique=True, nullable=False)
    menus = relationship(
        "Menu",
        secondary=association_table,
        back_populates="users")
