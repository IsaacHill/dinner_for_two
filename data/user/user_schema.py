from .user_model import User as UserModel
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnections(relay.Connection):
    class Meta:
        node = User
