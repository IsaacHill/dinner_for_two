"""Module to store the model of the user"""
from data.base import Base, association_table
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    """User Model"""

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String)
    created = Column(Date)
    last_login = Column(Date)
    admin = Column(Boolean)
    menus = relationship(
        "Menu",
        secondary=association_table,
        back_populates="users")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
