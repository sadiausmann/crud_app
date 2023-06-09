from flask import Blueprint
from controllers.sessions_controller import new, create, delete, index, recipe

sessions_routes = Blueprint('sessions_routes', __name__)

sessions_routes.route('/new')(new)
sessions_routes.route('', methods=["POST"])(create)
sessions_routes.route('/delete', methods=["POST"])(delete)
sessions_routes.route('/index')(index)
sessions_routes.route('/page/<id>')(recipe)