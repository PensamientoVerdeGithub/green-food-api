from ..models.ingredientes import Ingredientes
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class IngredientesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredientes