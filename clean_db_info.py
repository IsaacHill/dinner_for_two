import os
os.environ['DATABASE_URL'] = 'sqlite:///database.sqlite3'
from data.ingredient.ingredient_model import Ingredient
from data.recipe.recipe_model import Recipe
from data.menu.menu_model import Menu
from data.user.user_model import User
from data.base import Base, db_session, engine, association_table

Ingredient.__table__.drop(engine)
Recipe.__table__.drop(engine)
Menu.__table__.drop(engine)
User.__table__.drop(engine)
association_table.drop(engine)
db_session.commit()