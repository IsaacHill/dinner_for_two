"""Module for user mutations"""

import graphene
from .user_schema import User
from .user_model import User as UserModel
from data.base import db_session


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)
    ok = graphene.Boolean()

    def mutate(cls, info, **args):
        name = args.pop('name')
        email = args.pop('email')
        ok = True
        # print(email)
        user = UserModel(name=name, email=email)
        db_session.add(user)
        db_session.commit()
        return CreateUser(user=user, ok=ok)
