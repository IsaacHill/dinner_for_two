import os
from data.ingredient.ingredient_model import Ingredient
from data.recipe.recipe_model import Recipe
from data.menu.menu_model import Menu
from data.user.user_model import User
from data.base import Base, db_session, engine, association_table

for tbl in reversed(meta.sorted_tables):
    engine.execute(tbl.delete())
    
db_session.commit()

Base.metadata.create_all(bind=engine)
db_session.commit()