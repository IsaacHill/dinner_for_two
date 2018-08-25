from models import engine, db_session, Base, Recipe, Menu, User, Ingredient
Base.metadata.create_all(bind=engine)

billy = User(name = "billy bob", email="test@mail.com")
mandy = User(name = "mandy bob", email="gog@mail.com")


# name = Column(String, index=True)
# quantity = Column(Integer)
# recipie_id = Column(Integer, ForeignKey('recipe.id'))
# unit = Column(String)



beef_cheek = Ingredient(name = "Beef Cheek", quantity:2, unit:"KG")

beef_stew = Recipe(name="Beef Stew")
roast_chicken = Recipe(name="roast chicken")
mash = Recipe(name="mash")
sheppards_pie = Recipe(name="shepards pie")

recipe_book_one = Menu(name="Recipe Book one", recipes=[beef_stew,roast_chicken], users = [billy])
recipe_book_two = Menu(name="Recipe Book one", recipes=[mash,sheppards_pie], users = [mandy])

db_session.add(recipe_book_one)
# db_session.add(billy)
# db_session.add(mandy)
db_session.add(recipe_book_two)
db_session.commit()