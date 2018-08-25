import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Menu as MenuModel, Recipe as RecipeModel, User as UserModel, Ingredient as IngredientModel
# User as UserModel

class Menu(SQLAlchemyObjectType):
    class Meta:
        model = MenuModel
        interfaces = (relay.Node, )


class MenuConnections(relay.Connection):
    class Meta:
        node = Menu


class Recipe(SQLAlchemyObjectType):
    class Meta:
        model = RecipeModel
        interfaces = (relay.Node, )


class RecipeConnections(relay.Connection):
    class Meta:
        node = Recipe

class Ingredient(SQLAlchemyObjectType):
    class Meta:
        model = IngredientModel
        interfaces = (relay.Node, )

class IngredientConnections(relay.Connection):
    class Meta:
        node = Ingredient

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnections(relay.Connection):
    class Meta:
        node = User

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    # all_users = SQLAlchemyConnectionField(UserConnection)
    # Disable sorting over this field
    all_menus = SQLAlchemyConnectionField(MenuConnections, sort=None)
    all_recipes = SQLAlchemyConnectionField(RecipeConnections, sort=None)
    all_users = SQLAlchemyConnectionField(UserConnections, sort=None)


schema = graphene.Schema(query=Query)