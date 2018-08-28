from .ingredient_model import Ingredient as IngredientModel
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class Ingredient(SQLAlchemyObjectType):
    class Meta:
        model = IngredientModel
        interfaces = (relay.Node, )


class IngredientConnections(relay.Connection):
    class Meta:
        node = Ingredient