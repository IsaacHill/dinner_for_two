from .menu_model import Menu as MenuModel
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class Menu(SQLAlchemyObjectType):
    class Meta:
        model = MenuModel
        interfaces = (relay.Node, )


class MenuConnections(relay.Connection):
    class Meta:
        node = Menu
