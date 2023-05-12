from flask import render_template, request, redirect
from models.recipe import all_recipes, create_recipe, get_recipe, update_recipe, delete_recipe
from services.session_info import current_user

def index():
    recipes = all_recipes()
    return render_template('recipes/index.html',recipes=recipes)

def new():
    return render_template('recipes/new.html')

def create():
    user_id = request.form.get(current_user()['id'])
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    create_recipe(user_id, title, image_url, ingredients, recipe )
    return redirect('/sessions/index')

def edit(id):
    recipe = get_recipe(id)
    return render_template('recipes/edit.html',recipe=recipe)

def update(id):
    user_id =request.form.get(current_user['user_id'])
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    update_recipe(user_id, title, image_url, ingredients, recipe)
    return redirect('/sessions/index')

def delete(id):
    delete_recipe(id)
    return redirect('/sessions/index')