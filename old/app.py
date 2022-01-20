# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# Habilits with radar charts!
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


df = pd.read_csv('./pokedex_data/Pokemon_cleaned.csv', sep=',', index_col='name')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label('Pokémon'),
    dcc.Dropdown(
        options=[
            {'label': x, 'value': x}
            for x in df.index.values
        ],
        value=[],
        multi=False
    ),


], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)