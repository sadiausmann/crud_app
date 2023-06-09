from flask import render_template, request, redirect, session
from models.user import find_user_by_email
from models.recipe import all_recipes, get_recipe, all_comments, all_likes
from services.session_info import current_user
import bcrypt

def new():
    return render_template('sessions/new.html')

def create():
    email = request.form.get("email")
    password = request.form.get('password')
    user = find_user_by_email(email)
    if user == None:
        return redirect('/sessions/new')
    
    valid_password = bcrypt.checkpw(password.encode(),user['password_digest'].encode())
    if valid_password:
        session['user_id'] = user['id']
        return redirect('/')
    else:
        return redirect('/sessions/new')
    
def delete():
    session.clear()
    return redirect('/recipes')

def index():
    recipes = all_recipes()
    return render_template('recipe/index.html', recipes=recipes,current_user= current_user())

def recipe(id):
    recipe = get_recipe(id)
    comments = all_comments(id)
    likes_count = all_likes(id)[0]
    return render_template('sessions/recipe.html', recipe=recipe,current_user= current_user(), comments = comments, likes_count = likes_count)