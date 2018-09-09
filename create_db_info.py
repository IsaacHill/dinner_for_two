
import os
os.environ['DATABASE_URL'] = 'sqlite:///database.sqlite3'
from data.ingredient.ingredient_model import Ingredient
from data.recipe.recipe_model import Recipe
from data.menu.menu_model import Menu
from data.user.user_model import User
from data.base import Base, db_session, engine

Base.metadata.create_all(bind=engine)

billy = User(name="Billy Bob",
             email="test@mail.com",
             password='123',
             admin=False
             )
mandy = User(name="Mandy Bob",
             email="gog@mail.com",
             password='321',
             admin=False
             )


beef_cheek = Ingredient(name="Beef Cheek", quantity=2.0, unit="KG")
onions = Ingredient(name="Onion", quantity=2.5, unit="")
butter = Ingredient(name="Butter", quantity=300.00, unit="KG")
bacon = Ingredient(name="Bacon", quantity=300.00, unit="KG")
potato = Ingredient(name="potato", quantity=6.0, unit="")
chicken = Ingredient(name="Chicken", quantity=5.0, unit="KG")

beef_stew = Recipe(name="Beef Stew",
                   method="Cook the stew",
                   time="1 Hour",
                   serves=2,
                   ingredients=[beef_cheek, onions])

roast_chicken = Recipe(name="Roast Chicken",
                       method="Roast it up good",
                       time="30 minutes",
                       serves=4,
                       ingredients=[chicken])

mash = Recipe(name="Mash",
              method="Mash Mash Mash",
              time="15 Minutes",
              serves=4,
              ingredients=[potato])

shepherds_pie = Recipe(name="shepherd's pie",
                       method="Where did double shepherd go",
                       time="2 hours",
                       serves=6,
                       ingredients=[bacon, potato])

recipe_book_one = Menu(name="Recipe Book One",
                       recipes=[beef_stew, roast_chicken],
                       users=[billy])

recipe_book_two = Menu(name="Recipe Book Two",
                       recipes=[mash, shepherds_pie],
                       users=[mandy])

db_session.add(recipe_book_one)
db_session.add(recipe_book_two)
db_session.commit()
