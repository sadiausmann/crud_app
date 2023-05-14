from flask import render_template, request, redirect, session
from models.recipe import all_recipes, create_recipe, get_recipe, update_recipe, delete_recipe, like_recipe, comment_recipe, all_comments
from services.session_info import current_user

def index():
    recipes = all_recipes()
    return render_template('recipes/index.html',recipes=recipes, current_user = current_user())

def new():
    return render_template('recipes/new.html')

def create():
    user_id = current_user()['id']
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    create_recipe(user_id, title, image_url, ingredients, recipe )
    return redirect(f'/recipes')

def edit(id):
    recipe = get_recipe(id)
    return render_template('recipes/edit.html',recipe=recipe)

def update(id):
    user_id = current_user()['id']
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    update_recipe(user_id, title, image_url, ingredients, recipe, id)
    return redirect(f'/sessions/page/{id}')

def delete(id):
    delete_recipe(id)
    return redirect('/recipes')

def like(id):
    like_recipe(id, session['user_id'])
    return redirect(f'/sessions/page/{id}')

def comments():
    comments = all_comments
    return render_template('session/recipe.html',current_user=current_user(), comments= comments, comment=comment)

def comment(id):
    recipe_id = id
    user_id = current_user()['id']
    comment = request.form.get('comment')
    comment_recipe(recipe_id, user_id, comment)
    return redirect(f'/sessions/page/{id}')

