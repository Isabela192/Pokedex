from models import Pokemon
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class PokemonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
