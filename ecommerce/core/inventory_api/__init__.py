from flask import Blueprint
# from . import routes 
inventory_category_api_blueprint = Blueprint('inventory_category_api', __name__)

from . import routes
