"""Module for user mutations"""

import graphene
from .user_schema import User
from .user_model import User as UserModel
from data.base import db_session
from sqlalchemy import exc
import datetime


class CreateUser(graphene.Mutation):
    """Create a user and add to db"""
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(cls, info, **args):
        name = args.pop('name')
        email = args.pop('email')
        password = args.pop('password')

        ok = False
        error = ''
        user = None
        if not UserModel.find_user(email):
            # create the new user
            user = UserModel(name=name, email=email, password=password)
            user.created = datetime.datetime.now()
            user.admin = False
            user.last_login = datetime.datetime.now()
            user.save_to_db()
            ok = True
        else:
            error = 'A user with that email already exists.'

        return CreateUser(user=user, ok=ok, error=error)


class RemoveUser(graphene.Mutation):
    """Remove a user mutation based on email and username"""
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    description = graphene.String()

    def mutate(self, info, **args):
        name = args.pop('name')
        email = args.pop('email')
        user = UserModel.query.filter_by(name=name, email=email).first()

        description = ''
        ok = False
        if user is not None:
            user.remove_from_db()
            ok = True
        else:
            description = 'Unable to find user in db'
        return RemoveUser(ok=ok, description=description)


class UserLogin(graphene.Mutation):
    """Main user login that returns jwt if user has correctly logged in"""
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()
    token = graphene.String()
    error = graphene.String()

    def mutate(self, info, **args):
        email = args.pop('email')
        password = args.pop('password')

        # retrieve user from db
        user = UserModel.query.filter_by(email=email).first()

        # setup variables
        error = ''
        token = ''
        ok = False
        if user is not None:
            if user.check_password(password):
                ok = True
                # TODO setup jwt here
            else:
                error = 'User credentials do not match.'
        else:
            error = 'User not found.'

        return UserLogin(ok=ok, token=token, error=error)

