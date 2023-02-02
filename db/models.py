from dataclasses import dataclass

from extensions import db_connect


@dataclass
class Pokemon(db_connect.Model):
    __tablename__ = 'POKEMON'

    id = db_connect.Column(db_connect.Integer, primary_key=True)
    name = db_connect.Column(db_connect.String)
    type1 = db_connect.Column(db_connect.String)
    type2 = db_connect.Column(db_connect.String)
    abilities = db_connect.Column(db_connect.String)
    against_bug = db_connect.Column(db_connect.Float)
    against_dark = db_connect.Column(db_connect.Float)
    against_dragon = db_connect.Column(db_connect.Float)
    against_electric = db_connect.Column(db_connect.Float)
    against_fairy = db_connect.Column(db_connect.Float)
    against_fight = db_connect.Column(db_connect.Float)
    against_fire = db_connect.Column(db_connect.Float)
    against_flying = db_connect.Column(db_connect.Float)
    against_ghost = db_connect.Column(db_connect.Float)
    against_grass = db_connect.Column(db_connect.Float)
    against_ground = db_connect.Column(db_connect.Float)
    against_ice = db_connect.Column(db_connect.Float)
    against_normal = db_connect.Column(db_connect.Float)
    against_poison = db_connect.Column(db_connect.Float)
    against_psychic = db_connect.Column(db_connect.Float)
    against_rock = db_connect.Column(db_connect.Float)
    against_steel = db_connect.Column(db_connect.Float)
    against_water = db_connect.Column(db_connect.Float)
    attack = db_connect.Column(db_connect.Float)
    base_egg_steps = db_connect.Column(db_connect.Float)
    base_happiness = db_connect.Column(db_connect.Float)
    base_total = db_connect.Column(db_connect.Float)
    capture_rate = db_connect.Column(db_connect.Integer)
    classfication = db_connect.Column(db_connect.String)
    defense = db_connect.Column(db_connect.Integer)
    experience_growth = db_connect.Column(db_connect.Integer)
    height_m = db_connect.Column(db_connect.Float)
    hp = db_connect.Column(db_connect.Integer)
    percentage_male = db_connect.Column(db_connect.Float)
    pokedex_number = db_connect.Column(db_connect.Integer)
    sp_attack = db_connect.Column(db_connect.Integer)
    sp_defense = db_connect.Column(db_connect.Integer)
    speed = db_connect.Column(db_connect.Integer)
    weight_kg = db_connect.Column(db_connect.Float)
    generation = db_connect.Column(db_connect.Integer)
    is_legendary = db_connect.Column(db_connect.Integer)

    def __repr__(self) -> str:
        return f'Pokemon {self.name} is from {self.generation}!'
