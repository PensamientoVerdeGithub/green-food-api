from flask import Blueprint, jsonify
from ..models.ingredientes import Ingredientes
from ..schema.Ingredientes import IngredientesSchema

ingredientes_blueprint = Blueprint('ingredientes', __name__)

@ingredientes_blueprint.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    ingredientes = Ingredientes.query.all()
    return jsonify(IngredientesSchema(many=True).dump(ingredientes))