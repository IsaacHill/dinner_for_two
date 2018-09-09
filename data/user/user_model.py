"""Module to store the model of the user"""
from data.base import Base, association_table, db_session
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    """User Model"""

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String)
    created = Column(DateTime, default=func.now())
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

    @classmethod
    def find_user(cls, email):
        """Returns user with the matched email"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def user_by_id(cls, user_id):
        """Returns user with the matched id"""
        return cls.query.filter_by(id=user_id).first()

    def set_password(self, password):
        """Sets user password with a hash"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """checks if the given password will match the stored password"""
        return check_password_hash(self.password, password)

    def save_to_db(self):
        """Saves the user object to the db"""
        db_session.add(self)
        db_session.commit()

    def remove_from_db(self):
        """Removes the user object from the db"""
        db_session.delete(self)
        db_session.commit()
