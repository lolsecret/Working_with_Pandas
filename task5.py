# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import pandas as pd
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go

df = pd.read_excel('task_4_input.xlsx')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

fig1 = px.bar(df, x="Name", y="City", color="City", barmode="group")
fig2 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
fig3 = {'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ]
        }
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(className='row', children=[
    html.H1(
        "Database analysis (First dashboard)",
        style={
            'display': 'inline-block',
            'width': '25%',
            'font-size': '50px',
            'text-align': 'center',
        }
    ),
    html.H1(
        "Database analysis (Second dashboard)",
        style={
            'display': 'inline-block',
            'width': '25%',
            'font-size': '50px',
            'text-align': 'center',
        }
    ),
    html.H1(
        "Database analysis (Third dashboard)",
        style={
            'display': 'inline-block',
            'width': '25%',
            'font-size': '50px',
            'text-align': 'center',
        }
    ),
    html.H1(
        "Database analysis (Fourth dashboard)",
        style={
            'display': 'inline-block',
            'width': '25%',
            'font-size': '50px',
            'text-align': 'center',
        }
    ),
    html.Div(children=[
        dcc.Graph(id="graph1", figure=fig1, style={'display': 'inline-block', 'width': '25%'}),
        dcc.Graph(id="graph2", style={'display': 'inline-block', 'width': '25%'}),
        dcc.Graph(id='graph3', figure=fig3, style={'display': 'inline-block', 'width': '50%'}),
        dcc.Graph(id='graph4', figure=fig2, style={'display': 'inline-block', 'width': '75%'}),
        dcc.Graph(id="graph5", figure=fig1, style={'display': 'inline-block', 'width': '25%'}),
    ]),

])



if __name__ == '__main__':
    app.run_server(debug=True)