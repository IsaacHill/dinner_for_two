"""Module for graphql schema"""

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from data.menu.menu_schema import MenuConnections
from data.user.user_schema import UserConnections, User
from data.user.user_mutation import CreateUser, RemoveUser, UserLogin, UserInformation
from data.menu.menu_mutation import AddMenu
from data.recipe.recipe_mutation import AddRecipe, RemoveRecipe
from data.recipe.recipe_schema import RecipeConnections
# import required to know about ingredients field - don't think i like this
from data.ingredient.ingredient_schema import IngredientConnections


class MyConnectionField(SQLAlchemyConnectionField):
    RELAY_ARGS = ['first', 'last', 'before', 'after']

    @classmethod
    def get_query(cls, model, info, **args):
        query = super(MyConnectionField, cls).get_query(model, info, **args)
        for field, value in args.items():
            if field not in cls.RELAY_ARGS:
                query = query.filter(getattr(model, field) == value)
        return query


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_menus = SQLAlchemyConnectionField(MenuConnections, sort=None)
    all_recipes = SQLAlchemyConnectionField(RecipeConnections, sort=None)
    all_users = MyConnectionField(UserConnections, email=graphene.String(), name=graphene.String(), sort=None)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    remove_user = RemoveUser.Field()
    user_login = UserLogin.Field()
    user_information = UserInformation.Field()
    add_menu = AddMenu.Field()
    add_recipe = AddRecipe.Field()
    remove_recipe = RemoveRecipe.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)