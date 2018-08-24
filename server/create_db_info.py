from models import engine, db_session, Base, Recipe, Menu
Base.metadata.create_all(bind=engine)

 # Fill the tables with some data
beef_stew = Recipe(name="Beef Stew")
roast_chicken = Recipe(name="roast chicken")
mash = Recipe(name="mash")
sheppards_pie = Recipe(name="shepards pie")

recipe_book_one = Menu(name="Recipe Book one", recipes=[beef_stew,roast_chicken])
recipe_book_two = Menu(name="Recipe Book one", recipes=[mash,sheppards_pie])

db_session.add(recipe_book_one)
db_session.add(recipe_book_two)
db_session.commit()