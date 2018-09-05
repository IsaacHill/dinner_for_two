from .user_model import User as UserModel
from graphene import relay, Int, resolve_only_args
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    """User Node"""
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
        exclude_fields = 'password'

    user_id = Int()

    @resolve_only_args
    def resolve_user_id(self):
        return self.id


class UserConnections(relay.Connection):
    class Meta:
        node = User
