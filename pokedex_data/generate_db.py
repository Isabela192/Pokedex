import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("sqlite:///pokedex.db")

df = pd.read_csv("/Users/isabela/Documents/case_studies/Pokedex/pokedex_data/Pokemon_cleaned.csv", delimiter=",")

df.to_sql(con=engine, if_exists="replace", name="pokemon")

