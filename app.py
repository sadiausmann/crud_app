import os
from flask import Flask, render_template
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from services.session_info import current_user

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return render_template('recipes/index.html', current_user= current_user())






