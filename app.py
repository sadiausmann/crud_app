import os
from flask import Flask, redirect
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from routes.recipes_routes import recipes_routes


SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')
app.register_blueprint(recipes_routes, url_prefix='/recipes')

@app.route('/')
def index():
    return redirect('/recipes')






