"""Module for menu mutations"""

import graphene
from .recipe_schema import Recipe
from .recipe_model import Recipe as RecipeModel
from..ingredient.ingredient_model import Ingredient as IngredientModel
from flask_graphql_auth import jwt_required, get_jwt_identity
from ..ingredient.ingredient_model import Ingredient
import datetime


class IngredientInput(graphene.InputObjectType):
    """Defines the inputs available for an ingredient"""
    name = graphene.String(description="Name of the ingredient")
    quantity = graphene.Float(description="Quantity of the ingredient")
    unit = graphene.String(description="Unit of the ingredient quantity, lb, grams, etc")


class RecipeInput(graphene.InputObjectType):
    """Defines the inputs available for a recipe"""
    name = graphene.String(description="Name of the recipe")
    menu_id = graphene.Int(description="ID of the associated menu")
    method = graphene.String(description="Method of the recipe")
    time = graphene.String(description="Time taken to complete the recipe")
    serves = graphene.Int(description="Number of adults the recipe serves")
    equipment = graphene.String(description="Specialised equipment needed")
    comments = graphene.String(description="User comments")
    ingredients = graphene.List(IngredientInput)


class AddRecipe(graphene.Mutation):
    """Mutation to add a recipe to a users menu"""
    class Arguments:
        input = RecipeInput(required=True)

    ok = graphene.Boolean(description='If the recipe creation was successful or not')
    recipe = graphene.Field(lambda: Recipe, description='Recipe created by this mutation')

    def mutate(self, info, **args):
        # Retrieve the recipe from args
        recipe_info = args.get('input')

        recipe = RecipeModel(name=recipe_info.name,
                             menu_id=recipe_info.menu_id,
                             method=recipe_info.method,
                             time=recipe_info.time,
                             serves=recipe_info.serves,
                             equipment=recipe_info.equipment,
                             comments=recipe_info.comments)

        for ingredient_info in recipe_info.ingredients:
            ingredient = IngredientModel(name=ingredient_info.name,
                                         quantity=ingredient_info.quantity,
                                         unit=ingredient_info.unit)
            recipe.ingredients.append(ingredient)
        recipe.save_to_db()

        return AddRecipe(ok=True, recipe=recipe)


class UpdateRecipe(graphene.Mutation):
    """Mutation to update an existing recipe"""
    class Arguments:
        recipe_id = graphene.Int(required=True, description="Recipe ID for the recipe")
        input = RecipeInput(description="Updated details for the recipe")


    ok = graphene.Boolean(description="If the recipe was correctly updated or not")
    recipe = graphene.Field(lambda: Recipe, description="The updated recipe")

    def mutate(self, info, **args):
        recipe_id = args.get('recipeId')
        recipe_info = args.get('input')
        recipe = RecipeModel.recipe_by_id(recipe_id)
        # TODO update the recipe record

class RemoveRecipe(graphene.Mutation):
    """Mutation to update an existing recipe"""
    class Arguments:
        recipe_id = graphene.Int(required=True, description="Recipe ID for the recipe")

    ok = graphene.Boolean(description="If the recipe was correctly removed or not")

    def mutate(self, info, **args):
        recipe_id = args.get('recipeId')
        recipe = RecipeModel.recipe_by_id(recipe_id)
        recipe.remove_from_db()
        ok = True
        return RemoveRecipe(ok=ok)