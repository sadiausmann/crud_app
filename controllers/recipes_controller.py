from flask import render_template, request, redirect, session
from models.recipe import all_recipes, create_recipe, get_recipe, update_recipe, delete_recipe, like_recipe
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
    return redirect('/sessions/index')

def edit(id):
    recipe = get_recipe(id)
    return render_template('recipes/edit.html',recipe=recipe)

def update(id):
    title = request.form.get('title')
    image_url = request.form.get('image_url')
    ingredients = request.form.get('ingredients')
    recipe = request.form.get('recipe')
    update_recipe(title, image_url, ingredients, recipe, id)
    return redirect('/sessions/index')

def delete(id):
    delete_recipe(id)
    return redirect('/sessions/index')

def like(id):
    like_recipe(id, session['user_id'])
    return redirect(f'/sessions/page/{id}')