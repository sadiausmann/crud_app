from flask import Blueprint
from controllers.recipes_controller import index, new, create, edit, update, delete

recipes_routes = Blueprint('recipes_routes', __name__)

recipes_routes.route('')(index)
recipes_routes.route('/new')(new)
recipes_routes.route('',methods=['POST'])(create)
recipes_routes.route('/<id>/edit')(edit)
recipes_routes.route('/<id>', methods=["POST"])(update)
recipes_routes.route('/<id>/delete', methods=["POST"])(delete) 