"""Module for graphql schema"""

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from data.user.user_schema import UserConnections
from data.menu.menu_schema import MenuConnections
from data.recipe.recipe_schema import RecipeConnections
# import required to know about ingredients field - don't think i like this
from data.ingredient.ingredient_schema import IngredientConnections


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_menus = SQLAlchemyConnectionField(MenuConnections, sort=None)
    all_recipes = SQLAlchemyConnectionField(RecipeConnections, sort=None)
    all_users = SQLAlchemyConnectionField(UserConnections, sort=None)


schema = graphene.Schema(query=Query)