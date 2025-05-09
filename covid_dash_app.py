import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load and prepare data
df = pd.read_csv('dataset/owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize Dash app
app = dash.Dash(__name__)
available_countries = sorted(df['location'].unique())

app.layout = html.Div([
    html.H1('COVID-19 Global Data Tracker Dashboard'),
    html.Div([
        html.Label('Select Countries:'),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': c, 'value': c} for c in available_countries],
            value=['Kenya', 'United States', 'India'],
            multi=True
        )
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        html.Label('Select Date Range:'),
        dcc.DatePickerRange(
            id='date-range',
            min_date_allowed=df['date'].min(),
            max_date_allowed=df['date'].max(),
            start_date=df['date'].min(),
            end_date=df['date'].max()
        )
    ], style={'width': '48%', 'display': 'inline-block', 'float': 'right'}),
    dcc.Graph(id='cases-deaths-graph'),
    dcc.Graph(id='vaccinations-graph')
])

@app.callback(
    Output('cases-deaths-graph', 'figure'),
    Output('vaccinations-graph', 'figure'),
    Input('country-dropdown', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_graphs(selected_countries, start_date, end_date):
    dff = df[df['location'].isin(selected_countries)]
    dff = dff[(dff['date'] >= pd.to_datetime(start_date)) & (dff['date'] <= pd.to_datetime(end_date))]
    
    fig1 = px.line(
        dff,
        x='date',
        y=['total_cases', 'total_deaths'],
        color='location',
        labels={'value': 'Count', 'variable': 'Metric'},
        title='Total Cases and Deaths Over Time'
    )
    fig2 = px.line(
        dff,
        x='date',
        y='total_vaccinations',
        color='location',
        labels={'total_vaccinations': 'Total Vaccinations'},
        title='Vaccination Rollout Over Time'
    )
    return fig1, fig2

if __name__ == '__main__':
    app.run(debug=True)
