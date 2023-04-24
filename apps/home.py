import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash import html, Input, Output, dash_table, dcc

from app import app

df = pd.read_csv('final_fully_cleaned_vehicle_details.csv')
df['Reg Date'] = pd.to_datetime(df['Reg Date'])
years = [{'label': str(year), 'value': year} for year in sorted(df['Reg Date'].dropna().dt.year.unique())]
vehicle_types = [{'label': str(vehicle_type), 'value': vehicle_type} for vehicle_type in
                 sorted(df['Vehicle Type'].unique())]
vehicle_status = [{'label': str(vehicle_statu), 'value': vehicle_statu} for vehicle_statu in
                  sorted(df['Vehicle Status'].unique())]
selling_types = [{'label': str(selling_type), 'value': selling_type} for selling_type in
                 sorted(df['Selling Type'].unique())]
df['Brand Name'] = df['Brand Name'].astype(str)
brand_names = [{'label': brand, 'value': brand} for brand in sorted(df['Brand Name'].unique())]

df['Posted Date'] = pd.to_datetime(df['Posted Date'])
df = df.sort_values(by='Posted Date', ascending=False)
number_of_vehicles = [{'label': str(i), 'value': i} for i in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]]
df['Mileage (Km)'].fillna(0, inplace=True)

print(brand_names)
layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.H5('Vehicle Details Filter', className='text-center',
                        style={'color': 'lightgrey'})
            ], className='col-md-12 container-fluid mx-auto'),

            html.Div([
                html.Label("Mileage Range:"),
                dcc.RangeSlider(
                    id='mileage-range-slider',
                    min=df['Mileage (Km)'].min(),
                    max=df['Mileage (Km)'].max(),
                    value=[df['Mileage (Km)'].min(), df['Mileage (Km)'].max()],
                    tooltip={"placement": "top", "always_visible": True},
                    marks={i: f'{i} km' for i in
                           range(int(df['Mileage (Km)'].min()), int(df['Mileage (Km)'].max()),
                                 int(int(df['Mileage (Km)'].max()) / 5))},
                    # step=,

                    allowCross=False,
                    updatemode='drag',
                    className='mb-4 mileage-slider',
                    persistence=True,
                    persistence_type='local',
                    vertical=False,
                    verticalHeight=900,
                    pushable=1000,
                    included=True,
                ),
            ], className='col-md-6'),

            html.Div([
                html.Label("Engine Capacity Range:"),
                dcc.RangeSlider(
                    id='capacity-range-slider',
                    min=df['Engine Capacity (cc)'].min(),
                    max=df['Engine Capacity (cc)'].max(),
                    value=[df['Engine Capacity (cc)'].min(), df['Engine Capacity (cc)'].max()],
                    tooltip={"placement": "top", "always_visible": True},
                    marks={i: f'{i} cc' for i in
                           range(int(df['Engine Capacity (cc)'].min()), int(df['Engine Capacity (cc)'].max()) + 1,
                                 2614)},
                    step=int(df['Engine Capacity (cc)'].max()) / 6,
                    allowCross=False,
                    updatemode='drag',
                    className='mb-4 mileage-slider1',
                    persistence=True,
                    persistence_type='local',
                    vertical=False,
                    verticalHeight=900,
                    pushable=1000,
                    included=True,
                ),
            ], className='col-md-6'),

            html.Div([
                "Year : ",
                dcc.Dropdown(
                    id='my-dropdown_year',
                    options=[{'label': 'All years', 'value': 'all'}] + years,
                    value='all',
                    className='dark-theme'
                ),
            ], className='col-md-4', style={'color': 'lightgrey'}),
            html.Div([
                "Vehicle Types : ",
                dcc.Dropdown(
                    id='my-dropdown_type',
                    options=[{'label': 'All types', 'value': 'all'}] + vehicle_types,
                    value='all',
                    className='dark-theme'
                ),
            ], className='col-md-4', style={'color': 'lightgrey'}),
            html.Div([
                "Vehicle Status : ",
                dcc.Dropdown(
                    id='my-dropdown_status',
                    options=[{'label': 'All', 'value': 'all'}] + vehicle_status,
                    value='all',
                    className='dark-theme'
                ),
            ], className='col-md-4', style={'color': 'lightgrey'}),

            html.Div([
                "Date Range : ",
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=df['Posted Date'].min(),
                    max_date_allowed=df['Posted Date'].max(),
                    initial_visible_month=df['Posted Date'].max(),
                    start_date=df['Posted Date'].min(),
                    end_date=df['Posted Date'].max(),
                    className='dark-theme2'
                ),
            ], className='col-md-4', style={'padding-top': '10px', 'color': 'lightgrey'}),

            html.Div([
                "Selling Type : ",
                dcc.Dropdown(
                    id='my-dropdown_selling_types',
                    options=[{'label': 'All selling types', 'value': 'all'}] + selling_types,
                    value='all',
                    className='dark-theme'
                ),
            ], className='col-md-4', style={'color': 'lightgrey'}),

        ], className='row mt-3 filter_by_year_div'),
        html.Div([
            dash_table.DataTable(
                id='my-table',
                data=df.to_dict('records'),
                page_size=11,
                style_table={
                    'maxHeight': '600px',
                    'overflowY': 'scroll',
                    'border': '3px solid grey',
                    'borderCollapse': 'collapse'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '5px',
                    'fontSize': '11px',
                    'font-family': 'sans-serif',
                    'border': '1px solid grey'
                },
                # filter_action='native',
                editable=True,
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'border': '1px solid black',
                    'textAlign': 'center',
                    'fontSize': '16px',
                    'font-family': 'sans-serif'
                },
                style_data={
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'lightgrey'
                },
            ),
        ], className='col-md-12', style={'padding-top': '10px'}),
    ], className='container-fluid', style={
        "border": "2px solid gray",
    }, ),
    html.Hr(),
    html.Div([
        html.Div([
            html.H5('Latest Vehicles', className='text-center',
                    style={'color': 'lightgrey'})
        ], className='col-md-12 container-fluid mx-auto'),
        html.Div([
            html.Div([
                "Number of vehicles: : ",
                dcc.Dropdown(
                    id='my-dropdown_vehicle_count',
                    options=number_of_vehicles,
                    value=12,
                    className='dark-theme'
                )
            ], className='col-md-4', style={'color': 'lightgrey'}),
            html.Div([
                "Vehicle Types : ",
                dcc.Dropdown(
                    id='my-dropdown_type_latest',
                    options=[{'label': 'All types', 'value': 'all'}] + vehicle_types,
                    value='all',
                    className='dark-theme'
                )
            ], className='col-md-4', style={'color': 'lightgrey'}),
            html.Div([
                "Vehicle Status : ",
                dcc.Dropdown(
                    id='my-dropdown_status_latest',
                    options=[{'label': 'All', 'value': 'all'}] + vehicle_status,
                    value='all',
                    className='dark-theme'
                )
            ], className='col-md-4', style={'color': 'lightgrey'}),
        ], className='row'),

        html.Div(id="latest-vehicle", children=[
            html.Div(id='cards-container', children=[

            ], className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3",
                     style={'background-color': 'rgb(50, 50, 50)', 'border-radius': '10px',
                            'border-color': 'rgb(50, 50, 50)'})
        ], style={'padding-top': '10px'}),

        # Use the dark background color with the bg-dark class

    ], className='container-fluid bg-dark',
        style={'border': '2px solid gray', 'border-radius': '5px', 'padding-top': '10px'}),

    html.Hr(),
    html.Div([
        html.Div([
            html.H5('Compare vehicles by type', className='text-center mb-4')
        ], className='col-md-12 container-fluid mx-auto'),

        html.Div(children=[
            # Dropdown menu for selecting vehicle status
            html.Div([
                "Vehicle Status : ",
                dcc.Dropdown(
                    id='vehicle-status-dropdown',
                    options=[{'label': 'All', 'value': 'all'}] + vehicle_status,
                    value='all',
                    className='dark-theme'
                ),
            ], className='col-md-12'),

            html.Div([
                "Date Range : ",
                dcc.DatePickerRange(
                    id='my-date-picker-range_graph',
                    min_date_allowed=df['Posted Date'].min(),
                    max_date_allowed=df['Posted Date'].max(),
                    initial_visible_month=df['Posted Date'].max(),
                    start_date=df['Posted Date'].min(),
                    end_date=df['Posted Date'].max(),
                    className='dark-theme2'
                ),
            ], className='col-md-4', style={'padding-top': '10px', 'color': 'lightgrey'}),

            # Bar chart of vehicle prices
            html.Div([
                dcc.Graph(id='vehicle-price-bar-chart')
            ]),
        ], className="g-3"),

        html.Div([
            html.Div(children=[
                html.Div([
                    "Date Range : ",
                    dcc.DatePickerRange(
                        id='my-date-picker-range_graph2',
                        min_date_allowed=df['Posted Date'].min(),
                        max_date_allowed=df['Posted Date'].max(),
                        initial_visible_month=df['Posted Date'].max(),
                        start_date=df['Posted Date'].min(),
                        end_date=df['Posted Date'].max(),
                        className='dark-theme2'
                    ),
                ], className='col-md-4', style={'padding-top': '10px', 'color': 'lightgrey'}),

                html.Div([
                    "Brand Name: ",
                    dcc.Dropdown(
                        id='brand_dropdown',
                        options=[{'label': 'All', 'value': 'all'}] + brand_names,
                        value='all',
                        className='dark-theme',
                        placeholder="Select Brand"
                    ),
                ], className='col-md-6', style={'color': 'lightgrey'}),

                # Bar chart of vehicle prices
                html.Div([
                    dcc.Graph(id='vehicle-price-bar-chart-2')
                ]),
            ], className="g-3"),
        ], className='col-md-12')

    ], className='container-fluid', style={'border': '2px solid black', 'border-radius': '5px', 'padding-top': '10px'})
], className='container-fluid bg-dark')


@app.callback(
    Output('my-table', 'data'),
    Input('my-dropdown_year', 'value'),
    Input('my-dropdown_type', 'value'),
    Input('my-dropdown_status', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('mileage-range-slider', 'value'),
    Input('capacity-range-slider', 'value'),
    Input('my-dropdown_selling_types', 'value')
)
def update_table(year, vehicle_type, vehicle_status, start_date, end_date, miles_range, capacity_range, selling_type):
    # Check if date range is None before unpacking it
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    mileage_range = [miles_range[0], miles_range[1]]
    capacity_ran = [capacity_range[0], capacity_range[1]]
    filtered_df = df.loc[df['Posted Date'].between(*date_range)]

    filtered_df = filtered_df.loc[filtered_df['Engine Capacity (cc)'].between(*capacity_ran)]
    filtered_df = filtered_df.loc[filtered_df['Vehicle Status'] != 'sold']
    filtered_df = filtered_df.loc[filtered_df['Mileage (Km)'].between(*mileage_range)]
    if year != 'all':
        filtered_df = filtered_df.loc[filtered_df['Reg Date'].dt.year == int(year)]
    if vehicle_type != 'all':
        filtered_df = filtered_df.loc[filtered_df['Vehicle Type'] == vehicle_type]
    if vehicle_status != 'all':
        filtered_df = filtered_df.loc[filtered_df['Vehicle Status'] == vehicle_status]
    if selling_type != 'all':
        filtered_df = filtered_df.loc[filtered_df['Selling Type'] == selling_type]

    filtered_df = filtered_df.sort_values(by='Posted Date', ascending=False)
    return filtered_df.to_dict('records')


@app.callback(
    Output('latest-vehicle', 'children'),
    Input('my-dropdown_vehicle_count', 'value'),
    Input('my-dropdown_type_latest', 'value'),
    Input('my-dropdown_status_latest', 'value'),
)
def update_vehicle_latest(count, type_latest, status_latest):
    if type_latest != 'all' and status_latest != 'all':
        df1_filtered = df.loc[(df['Vehicle Type'] == type_latest) & (df['Vehicle Status'] == status_latest)]
    elif type_latest != 'all':
        df1_filtered = df.loc[df['Vehicle Type'] == type_latest]
    elif status_latest != 'all':
        df1_filtered = df.loc[df['Vehicle Status'] == status_latest]
    else:
        df1_filtered = df

    latest_cars = df1_filtered.iloc[:count]

    cards = [dbc.Card(
        dbc.CardBody([
            html.H5(f"{row['Model Name']} ({row['Vehicle Status']})", className="card-title mb-2 text-success"),
            html.Ul([
                html.Li(f"Price: {row['Prices ($)']}", className="card-text text-info"),
                html.Li(f"Depreciation: {row['Depreation ($)']}", className="card-text text-info"),
                # Fix typo in column name
                html.Li(f"Registration Date: {row['Reg Date']}", className="card-text text-info"),
                html.Li(f"Engine Capacity: {row['Engine Capacity (cc)']}", className="card-text text-info"),
                html.Li(f"Mileage: {row['Mileage (Km)']}", className="card-text text-info"),
                # Fix typo in column name and lowercase km
            ], className="list-unstyled mb-3"),
            html.A(dbc.Button("Learn More", color="primary", className="btn-sm"), href=row['Link of Vehicle']),
        ], className="p-3", style={'background-color': 'rgb(50, 50, 50)', 'border-radius': '10px',
                                   'border-color': 'rgb(50, 50, 50)'})
    ) for index, row in latest_cars.iterrows()]

    return dbc.Row(cards, className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3")


@app.callback(
    Output('vehicle-price-bar-chart', 'figure'),
    [
        Input('vehicle-status-dropdown', 'value'),
        Input('my-date-picker-range_graph', 'start_date'),
        Input('my-date-picker-range_graph', 'end_date'), ]
)
def update_vehicle_price_bar_chart(status, start_date, end_date):
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    filtered_df = df.loc[df['Posted Date'].between(*date_range)]
    if status == 'all':
        vehicle_type_counts = filtered_df['Vehicle Type'].value_counts()
        fig = go.Figure(go.Bar(x=vehicle_type_counts.index, y=vehicle_type_counts.values,
                               text=vehicle_type_counts.values, textposition='auto'))
    else:
        filtered_df = df[(df['Vehicle Status'] == status)]
        vehicle_type_counts = filtered_df['Vehicle Type'].value_counts()
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


@app.callback(
    Output('vehicle-price-bar-chart-2', 'figure'),
    [
        Input('brand_dropdown', 'value'),
        Input('my-date-picker-range_graph2', 'start_date'),
        Input('my-date-picker-range_graph2', 'end_date'), ]
)
def update_vehicle_price_bar_chart2(brand, start_date, end_date):
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    filtered_df = df.loc[df['Posted Date'].between(*date_range)]

    if brand == 'all':
        vehicle_type_counts = filtered_df['Vehicle Type'].value_counts()
        fig = go.Figure(go.Bar(x=vehicle_type_counts.index, y=vehicle_type_counts.values,
                               text=vehicle_type_counts.values, textposition='auto'))
    else:
        filtered_df = df[(df['Brand Name'] == brand)]
        vehicle_type_counts = filtered_df['Vehicle Type'].value_counts()
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
