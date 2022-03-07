from flask import Blueprint
from .route import ApiRoute
from .views import ApiViews

import os

api_blueprint = Blueprint(
    name="api_blueprint",
    import_name=__name__,
    static_folder=os.environ.get("STATIC_DIR"),
    template_folder=os.environ.get("TEMPLATES_DIR")
)
api_blueprint.add_url_rule("/", view_func=ApiRoute.main, methods=["GET", "POST"])
api_blueprint.add_url_rule("/insert", view_func=ApiViews.insert, methods=["POST"])
api_blueprint.add_url_rule("/update", view_func=ApiViews.update, methods=["POST"])
api_blueprint.add_url_rule("/select", view_func=ApiViews.select, methods=["POST"])
api_blueprint.add_url_rule("/delete", view_func=ApiViews.delete, methods=["POST"])
api_blueprint.add_url_rule("/logs", view_func=ApiViews.logs, methods=["POST", "GET"])
