"""Module for user mutations"""

import graphene
from .user_schema import User
from .user_model import User as UserModel
from flask_graphql_auth import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
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

    @jwt_required
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
    class Arguments(object):
        email = graphene.String()
        password = graphene.String()

    ok = graphene.Boolean()
    access_token = graphene.String()
    refresh_token = graphene.String()
    error = graphene.String()

    def mutate(self, info, email, password):
        # setup variables
        error = ''
        ok = False
        access_token = ''
        refresh_token = ''

        # retrieve user from db
        user = UserModel.find_user(email=email)

        if user is not None:
            if user.check_password(password):
                ok = True
                access_token = create_access_token(email)
                refresh_token = create_refresh_token(email)
            else:
                error = 'User credentials do not match.'
        else:
            error = 'User not found.'

        return UserLogin(ok=ok, error=error, access_token=access_token, refresh_token=refresh_token)


class UserInformation(graphene.Mutation):
    """User information response that returns general information on user"""
    class Arguments:
        email = graphene.String()
        token = graphene.String()

    message = graphene.String()

    @jwt_required
    def mutate(self, info, **args):
        print(get_jwt_identity())
        return UserInformation(message='protected')



