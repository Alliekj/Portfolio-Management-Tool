import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import requests
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='risk-aversion', type='number', placeholder='Risk Aversion'),
    dcc.Textarea(id='returns', placeholder='Enter returns data', style={'width': '100%', 'height': 200}),
    html.Button(id='submit-button', n_clicks=0, children='Optimize'),
    html.Div(id='output-weights')
])

@app.callback(
    Output('output-weights', 'children'),
    Input('submit-button', 'n_clicks'),
    State('risk-aversion', 'value'),
    State('returns', 'value')
)
def update_output(n_clicks, risk_aversion, returns):
    if n_clicks > 0:
        returns = pd.read_csv(pd.compat.StringIO(returns))
        data = {'returns': returns.values.tolist(), 'risk_aversion': risk_aversion}
        response = requests.post('http://127.0.0.1:5000/optimize', json=data)
        weights = response.json()
        return html.Div([html.P(f'Asset {i+1}: {weight:.2%}') for i, weight in enumerate(weights)])

if __name__ == '__main__':
    app.run_server(debug=True)

