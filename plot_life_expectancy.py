import plotly.express as px
import json
import plotly.utils
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np


def plot_on_map(dataset, meta, year):

    countries = dataset[['Country', meta, 'Year']]
    countries = countries[countries['Year'] == year]

    fig = px.choropleth(countries, locations="Country",
                        locationmode='country names',
                        color=meta,
                        hover_name="Country",
                        hover_data={
                            meta: True,
                            'Country': False
                        },
                        color_discrete_map={
                            'Developing': 'CadetBlue',
                            'Developed': 'DarkSalmon'
                        })
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def basic_plot(df, name):
    fig = make_subplots(rows=7, cols=3, subplot_titles=df.columns[3:])
    i = 1
    j = 1
    df = df[df['Country'] == name]
    for meta in df:
        if meta in ['Year', 'Status', 'Country']:
            continue
        fig.add_trace(
            go.Scatter(
                x=df.Year.unique(),
                y=np.transpose(df[[meta]]).squeeze(),
            ),
            row=i,
            col=j,
        )
        if j < 3:
            j += 1
        else:
            j = 1
            i += 1

    fig.update_layout(height=2500, width=1300, title_text="Data through years of " + name)
    fig.update(layout_showlegend=False)
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json


def plot_heatmap(df):

    corr = df.corr()
    fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale=px.colors.sequential.Mint)
    fig.update_layout(height=800, width=1200)
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json
