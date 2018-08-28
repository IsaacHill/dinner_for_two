from .recipe_model import Recipe as RecipeModel
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class Recipe(SQLAlchemyObjectType):
    class Meta:
        model = RecipeModel
        interfaces = (relay.Node, )


class RecipeConnections(relay.Connection):
    class Meta:
        node = Recipe
