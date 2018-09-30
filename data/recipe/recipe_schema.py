from .recipe_model import Recipe as RecipeModel
from graphene import relay
from graphene import relay, Int, resolve_only_args
from graphene_sqlalchemy import SQLAlchemyObjectType


class Recipe(SQLAlchemyObjectType):
    class Meta:
        model = RecipeModel
        interfaces = (relay.Node, )
    
    recipe_id = Int()

    @resolve_only_args
    def resolve_recipe_id(self):
        return self.id


class RecipeConnections(relay.Connection):
    class Meta:
        node = Recipe
