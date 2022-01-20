import pandas as pd
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine=db.create_engine('sqlite://')
df = pd.read_csv('./pokedex_data/Pokemon_cleaned.csv')

df.to_sql(name='pokemon',con=engine,if_exists='replace')

Session=sessionmaker(bind=engine)
session=Session()
meta= db.MetaData(engine)

pokemon=db.Table('pokemon', meta, autoload=True)

# Create a list of all the names of the pokemon
def pokenames():
    names = [name[0] for name in session.query(pokemon.c.name).all()]
    return names

# Create a list of all the types of the pokemon
def poketypes(name):
    columns=(pokemon.c.name, pokemon.c.type1, pokemon.c.type2)
    dbquery=session.query(pokemon).with_entities(*columns)
    dbquery=dbquery.filter(pokemon.c.name==name)
    types=pd.read_sql(dbquery.statement, engine, index_col='name')
    return types

def pokeweakness(name):
    '''
    In this dataset the pokemon against columns list the
    DAMAGE that that pokémon will take against that type
    So, if the pokemon is a grass type, it will take double damage
    from a fire type.
    '''
    columns=(pokemon.c.name, pokemon.c.against_bug, pokemon.c.against_dark,
             pokemon.c.against_dragon, pokemon.c.against_electric,
             pokemon.c.against_fairy, pokemon.c.against_fight,
             pokemon.c.against_fire, pokemon.c.against_flying,
             pokemon.c.against_ghost, pokemon.c.against_grass,
             pokemon.c.against_ground, pokemon.c.against_ice,
             pokemon.c.against_normal, pokemon.c.against_poison,
             pokemon.c.against_psychic, pokemon.c.against_rock,
             pokemon.c.against_steel, pokemon.c.against_water)
    dbquery=session.query(pokemon).with_entities(*columns)
    dbquery=dbquery.filter(pokemon.c.name==name)
    against_table=pd.read_sql(dbquery.statement, engine, index_col='name')
    weakness={}
    for key, value in against_table.items():
        for integer in value:
            if integer >=2:
                weakness[key]=integer
    return weakness

def pokestats(name):
    '''
    The stats of pokemon are given by the main stats of the pokemon:
        - HP: Hit points
        - Attack
        - Defense
        - Special Attack
        - Special Defense
        - Speed
    '''
    columns=(pokemon.c.name, pokemon.c.hp, pokemon.c.attack, 
             pokemon.c.defense, pokemon.c.sp_attack, 
             pokemon.c.sp_defense, pokemon.c.speed)
    dbquery=session.query(pokemon).with_entities(*columns)
    dbquery=dbquery.filter(pokemon.c.name==name)
    stats_table=pd.read_sql(dbquery.statement, engine, index_col='name')
    stats_table.columns=['HP', 'Attack', 'Defense', 'Sp Attackk', 'Sp Defense', 'Speed']
    stats=stats_table.stack().reset_index()
    stats.columns=['name', 'stat', 'value']
    return stats

def pokeskills(name):
    columns=(pokemon.c.name, pokemon.c.abilities)
    dbquery=session.query(pokemon).with_entities(*columns)
    dbquery=dbquery.filter(pokemon.c.name==name)
    skills=pd.read_sql(dbquery.statement, engine, index_col='name')
    return skills