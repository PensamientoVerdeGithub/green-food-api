from flask import Blueprint, Response
from ..models.ingredientes import Ingredientes
from ..schema.Ingredientes import IngredientesSchema

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def get_ingredientes():
     return Response("🥦", mimetype='text/plain')