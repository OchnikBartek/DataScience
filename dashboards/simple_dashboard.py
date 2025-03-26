import dash
from dash import dcc, html
import plotly.graph_objects as go


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2(children='Simple Dashboard'),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(x = ['styczen','luty','marzec'],
                   y = [1528,6783,392],
                   name = 'pierwszy kwartal w 2023'),
            go.Bar(x = ['styczen','luty','marzec'],
                   y = [7934,10987,12567],
                   name = 'pierwszy kwartal w 2024'),
        ])
    )
])

if __name__ == '__main__':
    app.run(debug=True)
