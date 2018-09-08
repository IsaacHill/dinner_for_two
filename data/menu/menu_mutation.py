"""Module for menu mutations"""

import graphene
from .menu_schema import Menu
from .menu_model import Menu as MenuModel
from ..user.user_model import User as UserModel
from flask_graphql_auth import jwt_required, get_jwt_identity
import datetime


class AddMenu(graphene.Mutation):
    """Create and add a menu for a user"""
    class Arguments:
        userID = graphene.Int(required=True, description="The internal ID of the User")
        name = graphene.String(required=True, description="Name of the menu being added")
        token = graphene.String(required=True, description="Access token associated with this user")

    ok = graphene.Boolean()
    error = graphene.String()
    menu = graphene.Field(lambda: Menu)

    @jwt_required
    def mutate(self, info, **args):
        user_id = args.get('userID')
        name = args.get('name')

        ok = False
        error = ''
        menu = None

        user = UserModel.user_by_id(user_id)
        if user is not None:
            if get_jwt_identity() == user.email:
                # we know that this user exists and is trying to make a menu
                menu = MenuModel(name=name)
                menu.created = datetime.datetime.now()
                user.menus.append(menu)
                menu.save_to_db()
                ok = True
            else:
                ok = False
                error = 'Not Authorized.'
        else:
            error = 'User unknown.'

        return AddMenu(ok=ok, error=error, menu=menu)