import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash import html, Input, Output, dash_table, dcc

font_awesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}]
external_stylesheets = [font_awesome, meta_tags,
                        'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

df = pd.read_csv('cleaned_vehicle_details.csv')
df['reg_date'] = pd.to_datetime(df['reg_date'])
years = [{'label': str(year), 'value': year} for year in sorted(df['reg_date'].dt.year.unique())]
vehicle_types = [{'label': str(vehicle_type), 'value': vehicle_type} for vehicle_type in
                 sorted(df['vehicle_type'].unique())]
vehicle_status = [{'label': str(vehicle_statu), 'value': vehicle_statu} for vehicle_statu in
                  sorted(df['status'].unique())]
df['posted_date'] = pd.to_datetime(df['posted_date'])

df1 = df.sort_values(by='posted_date', ascending=False)

# select the latest 8 cars
latest_cars = df1.iloc[:8]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Vehicle Data Analyzer', className='title_text ')
        ], className='title_container twelve columns')
    ], className='row flex_display ', style={'padding-bottom': '10px'}),
    html.Div([
        html.Div([
            html.Div([
                html.H5('Vehicle Details Filter by year, type and status', className='text-center')
            ], className='col-md-12 container-fluid mx-auto'),

            html.Div([
                "Year : ",
                dcc.Dropdown(
                    id='my-dropdown_year',
                    options=[{'label': 'All years', 'value': 'all'}] + years,
                    value='all',
                ),
            ], className='col-md-4'),
            html.Div([
                "Vehicle Types : ",
                dcc.Dropdown(
                    id='my-dropdown_type',
                    options=[{'label': 'All types', 'value': 'all'}] + vehicle_types,
                    value='all',
                ),
            ], className='col-md-4'),
            html.Div([
                "Vehicle Status : ",
                dcc.Dropdown(
                    id='my-dropdown_status',
                    options=[{'label': 'All', 'value': 'all'}] + vehicle_status,
                    value='all',
                ),
            ], className='col-md-4'),

            html.Div([
                "Date Range : ",
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=df['posted_date'].min(),
                    max_date_allowed=df['posted_date'].max(),
                    initial_visible_month=df['posted_date'].max(),
                    start_date=df['posted_date'].min(),
                    end_date=df['posted_date'].max()
                ),
            ], className='col-md-4', style={'padding-top': '10px'}),

        ], className='row mt-3 filter_by_year_div'),
        html.Div([
            dash_table.DataTable(
                id='my-table',
                data=df.to_dict('records'),
                page_size=11,
                style_table={
                    'maxHeight': '600px',
                    'overflowY': 'scroll',
                    'border': 'thin lightgrey solid',
                    'borderCollapse': 'collapse'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '5px',
                    'fontSize': '11px',
                    'font-family': 'sans-serif'
                },
                # filter_action='native',
                editable=True,
                style_header={
                    'backgroundColor': 'lightgrey',
                    'fontWeight': 'bold',
                    'border': 'thin lightgrey solid',
                    'textAlign': 'center',
                    'fontSize': '16px',
                    'font-family': 'sans-serif'
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    },
                    {
                        'if': {'state': 'active'},
                        'backgroundColor': 'rgba(0, 116, 217, 0.3)',
                        'border': '1px solid rgba(0, 116, 217, 1)'
                    },
                    {
                        'if': {'column_id': 'price'},
                        'textAlign': 'right',
                        'type': 'numeric',
                        'format': {'specifier': '.2f'}
                    }
                ]
            ),
        ], className='col-md-12', style={'padding-top': '10px'}),
    ], className='container-fluid', style={
        "border": "2px solid black",
    }, ),
    html.Hr(),
    html.Div([
        html.Div([
            html.H5('Latest vehicles', className='text-center mb-4')
        ], className='col-md-12 container-fluid mx-auto'),
        html.Div(id='cards-container', children=[
            dbc.Card(
                dbc.CardBody([
                    html.H5(f"{row['model_name']} ({row['status']})", className="card-title mb-2"),
                    html.Ul([
                        html.Li(f"Price: {row['prices']}", className="card-text"),
                        html.Li(f"Depreciation: {row['depreation']}", className="card-text"),
                        html.Li(f"Registration Date: {row['reg_date']}", className="card-text"),
                        html.Li(f"Engine Capacity: {row['eng_cap']}", className="card-text"),
                        html.Li(f"Mileage: {row['mileage']}", className="card-text"),
                    ], className="list-unstyled mb-3"),
                    dbc.Button("Learn More", color="primary", className="btn-sm"),
                ], className="p-3 shadow-sm")
            ) for index, row in latest_cars.iterrows()
        ], className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3")

    ], className='container-fluid', style={'border': '2px solid black', 'border-radius': '5px', 'padding-top': '10px'}),
    html.Hr(),
    html.Div([
        html.Div([
            html.H5('Compare vehicles by type', className='text-center mb-4')
        ], className='col-md-12 container-fluid mx-auto'),

        html.Div(id='cards-container', children=[
            # Dropdown menu for selecting vehicle status
            html.Div([
                "Vehicle Status : ",
                dcc.Dropdown(
                    id='vehicle-status-dropdown',
                    options=[{'label': 'All', 'value': 'all'}] + vehicle_status,
                    value='all',
                ),
            ], className='col-md-12'),

            # Bar chart of vehicle prices
            html.Div([
                dcc.Graph(id='vehicle-price-bar-chart')
            ]),
        ], className="g-3"),

    ], className='container-fluid', style={'border': '2px solid black', 'border-radius': '5px', 'padding-top': '10px'})
], className='container-fluid')


@app.callback(
    Output('my-table', 'data'),
    Input('my-dropdown_year', 'value'),
    Input('my-dropdown_type', 'value'),
    Input('my-dropdown_status', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
)
def update_table(year, vehicle_type, vehicle_status, start_date, end_date):
    # Check if date range is None before unpacking it
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    filtered_df = df.loc[df['posted_date'].between(*date_range)]
    filtered_df = filtered_df.loc[filtered_df['status'] != 'sold']
    if year != 'all':
        filtered_df = filtered_df.loc[filtered_df['reg_date'].dt.year == int(year)]
    if vehicle_type != 'all':
        filtered_df = filtered_df.loc[filtered_df['vehicle_type'] == vehicle_type]
    if vehicle_status != 'all':
        filtered_df = filtered_df.loc[filtered_df['status'] == vehicle_status]
    filtered_df = filtered_df.sort_values(by='posted_date', ascending=False)
    return filtered_df.to_dict('records')


@app.callback(
    dash.dependencies.Output('vehicle-price-bar-chart', 'figure'),
    [
        dash.dependencies.Input('vehicle-status-dropdown', 'value')]
)
def update_vehicle_price_bar_chart(status):
    if status == 'all':
        vehicle_type_counts = df['vehicle_type'].value_counts()
        fig = go.Figure(go.Bar(x=vehicle_type_counts.index, y=vehicle_type_counts.values,
                               text=vehicle_type_counts.values, textposition='auto'))
    else:
        filtered_df = df[(df['status'] == status)]
        vehicle_type_counts = filtered_df['vehicle_type'].value_counts()
        fig = go.Figure(go.Bar(x=vehicle_type_counts.index, y=vehicle_type_counts.values,
                               text=vehicle_type_counts.values, textposition='auto'))

    fig.update_layout(
        xaxis_title="Vehicle Type",
        yaxis_title="Count",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin=dict(l=20, r=20, t=20, b=20),
        template='plotly_white',
        autosize=True,
        font=dict(family="Arial, sans-serif", size=14, color="#7f7f7f"))

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
