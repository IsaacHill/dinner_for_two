from data.ingredient.ingredient_model import Ingredient
from data.recipe.recipe_model import Recipe
from data.menu.menu_model import Menu
from data.user.user_model import User
from data.base import Base, db_session, engine

Base.metadata.create_all(bind=engine)

billy = User(name = "billy bob", email="test@mail.com")
mandy = User(name = "mandy bob", email="gog@mail.com")


beef_cheek = Ingredient(name = "Beef Cheek", quantity=2.0, unit="KG")
onions = Ingredient(name = "Onion", quantity=2.5, unit="")
butter = Ingredient(name = "Butter", quantity=300.00, unit="KG")
bacon = Ingredient(name = "Bacon", quantity=300.00, unit="KG")
potato = Ingredient(name = "potato", quantity=6.0, unit="")
potatos = Ingredient(name = "potato", quantity=6.0, unit="")
chicken = Ingredient(name = "Chicken", quantity=5.0, unit="KG")

beef_stew = Recipe(name="Beef Stew", ingredients = [beef_cheek,onions])
roast_chicken = Recipe(name="roast chicken", ingredients = [chicken])
mash = Recipe(name="mash", ingredients=[potatos])
sheppards_pie = Recipe(name="shepards pie", ingredients=[bacon,potato])

recipe_book_one = Menu(name="Recipe Book one", recipes=[beef_stew,roast_chicken], users = [billy])
recipe_book_two = Menu(name="Recipe Book one", recipes=[mash,sheppards_pie], users = [mandy])

db_session.add(recipe_book_one)
# db_session.add(billy)
# db_session.add(mandy)
db_session.add(recipe_book_two)
db_session.commit()