from .menu_model import Menu as MenuModel
from graphene import relay, resolve_only_args, Int
from graphene_sqlalchemy import SQLAlchemyObjectType


class Menu(SQLAlchemyObjectType):
    class Meta:
        model = MenuModel
        interfaces = (relay.Node, )

    menu_id = Int()

    @resolve_only_args
    def resolve_menu_id(self):
        return self.id


class MenuConnections(relay.Connection):
    class Meta:
        node = Menu
