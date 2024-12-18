from flask import Blueprint
from ..controller.user_controller import UserController

user_controller = UserController()

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

user_bp.route("/", methods=["GET"])(user_controller.get_users)

user_bp.route("/<int:id>", methods=["GET"])(user_controller.get_user)

user_bp.route("/", methods=["POST"])(user_controller.add_user)
