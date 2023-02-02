from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import tools


df = tools.pokestats('Pikachu')
# plot dos status já vem configurados na função pokestats
fig = px.line_polar(
    df,
    r='value',
    theta='stat',
    line_close=True,
    title='Pokemon Status',
    template='ggplot2',
)
fig.update_traces(fill='toself')
fig.show()
