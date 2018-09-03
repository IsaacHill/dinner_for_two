from .user_model import User as UserModel
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    """User Node"""
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
        exclude_fields = 'password'


class UserConnections(relay.Connection):
    class Meta:
        node = User
