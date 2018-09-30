""" Main module for server"""

from flask import Flask
from config import JWT_SECRET_KEY
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from flask_cors import CORS
from data.base import db_session
from data.schema import schema
import os

app = Flask(__name__)
auth = GraphQLAuth(app)
# app.debug = True

app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config["REFRESH_EXP_LENGTH"] = 30
app.config["ACCESS_EXP_LENGTH"] = 10

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    ),
)

cors = CORS(app, resources={"*": {"origins": os.environ['DOMAIN']}})

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()

