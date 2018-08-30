"""Module for user mutations"""

import graphene
from .user_schema import User
from .user_model import User as UserModel
from data.base import db_session


class CreateUser(graphene.Mutation):
    """Create a user and add to db"""
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()

    def mutate(cls, info, **args):
        name = args.pop('name')
        email = args.pop('email')
        user = UserModel(name=name, email=email)
        db_session.add(user)
        db_session.commit()
        ok = True
        return CreateUser(user=user, ok=ok)


class RemoveUser(graphene.Mutation):
    """Remove a user mutation based on email and username"""
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    description = graphene.String()

    def mutate(cls, info, **args):
        name = args.pop('name')
        email = args.pop('email')
        user = UserModel.query.filter_by(name=name, email=email).first()

        if user is not None:
            db_session.delete(user)
            db_session.commit()
            ok = True
            description = ''
        else:
            ok = False
            description = 'Unable to find user in db'
        return RemoveUser(ok=ok, description=description)

