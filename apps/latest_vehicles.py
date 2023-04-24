import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash import html, dash_table, dcc

from app import app

df_new = pd.read_csv('final_details.csv')
df_newly_added = pd.read_csv('final_new_details.csv')
df_newly_added['Brand Name'] = df_newly_added['Brand Name'].astype(str)
df_new['Posted Date'] = pd.to_datetime(df_new['Posted Date'])
dropdown_options = [{'label': x, 'value': x} for x in df_new['Brand Name'].unique()]
brand_names = [{'label': str(brand), 'value': brand} for brand in
               sorted(df_new['Brand Name'].unique())]

# Define a function to clean and convert the values to numbers
import re


def clean_and_convert(value):
    value = str(value).replace('$', '').replace(',', '').replace('/yr', '').replace('\n', '').strip()
    value = re.sub(r'[^\d.]+', '', value)
    if value == '..':
        return 0
    else:
        return float(value)


# Use apply function to apply the clean_and_convert function to all elements of the 'price' column
df_new['depreciation'] = df_new['depreciation'].apply(clean_and_convert)
df_new['price'] = df_new['price'].apply(clean_and_convert)

layout = html.Div([
    html.Div([
        html.Div([
            html.H5('All vehicle with full details', className='text-center',
                    style={'color': 'lightgrey'})
        ], className='col-md-12 container-fluid mx-auto'),
        dash_table.DataTable(
            id='my-table',
            data=df_new.to_dict('records'),
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
    html.Hr(),
    html.Div([
        html.Div([
            html.H5('Newly added vehicles', className='text-center',
                    style={'color': 'lightgrey'})
        ], className='col-md-12 container-fluid mx-auto'),
        html.Div([
            "Brand Name: ",
            dcc.Dropdown(
                id='brand_dropdown2',
                options=[{'label': 'All', 'value': 'all'}] + brand_names,
                value='all',
                className='dark-theme',
                placeholder="Select Brand"
            ),
        ], className='col-md-6', style={'color': 'lightgrey'}),
        html.Div(id="newly-added-vehicle", children=[
            html.Div(id='cards-container', children=[

            ], className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3",
                     style={'background-color': 'rgb(50, 50, 50)', 'border-radius': '10px',
                            'border-color': 'rgb(50, 50, 50)'})
        ], style={'padding-top': '10px'}),
    ], className='col-md-12', style={'padding-left': '20px'}),
    html.Hr(),
    html.Div(children=[
        html.Div([
            html.Div([
                html.H5('Vehicle Comparison', className='text-center',
                        style={'color': 'lightgrey'})
            ], className='col-md-12 container-fluid mx-auto'),
            # First row
            html.Div([
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-1', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Brand"
                    ),
                ], className='col-md-2', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-2', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Model"
                    ),
                ], className='col-md-2', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-3', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Other Name"
                    ),
                ], className='col-md-2', style={'color': 'lightgrey'}),
                html.Div([  # new column with button

                    html.Button('Add to comparison', id='first_add_button', n_clicks=0)
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([  # new column with button

                    html.Button('Clear Table', id='clear_button', n_clicks=0)
                ], className='col-md-3', style={'color': 'lightgrey'}),
            ], className="row mt-3"),
        ], className='col-md-12'),

        html.Div(id='comparison-table', style={'padding-top': '30px'})
    ], className='col-md-12'),
    html.Hr(),
    html.Div([
        html.Div(children=[
            html.Div([
                html.H5('Average Depreciation ($) by Vehicle Type', className='text-center',
                        style={'color': 'lightgrey'})
            ], className='col-md-12 container-fluid mx-auto'),
            html.Div([
                "Date Range : ",
                dcc.DatePickerRange(
                    id='my-date-picker-range_graph3',
                    min_date_allowed=df_new['Posted Date'].min(),
                    max_date_allowed=df_new['Posted Date'].max(),
                    initial_visible_month=df_new['Posted Date'].max(),
                    start_date=df_new['Posted Date'].min(),
                    end_date=df_new['Posted Date'].max(),
                    className='dark-theme2'
                ),
            ], className='col-md-4', style={'padding-top': '10px', 'color': 'lightgrey'}),

            html.Div([
                "Brand Name: ",
                dcc.Dropdown(
                    id='brand_dropdown3',
                    options=[{'label': 'All', 'value': 'all'}] + brand_names,
                    value='all',
                    className='dark-theme',
                    placeholder="Select Brand"
                ),
            ], className='col-md-6', style={'color': 'lightgrey'}),

            # Bar chart of vehicle prices
            html.Div([
                dcc.Graph(id='vehicle-price-bar-chart-3')
            ]),
        ], className="g-3"),
    ], className='col-md-12'),
    html.Hr(),
    html.Div([
        html.Div(children=[
            html.Div([
                html.H5('Average Price ($) by Vehicle Type', className='text-center',
                        style={'color': 'lightgrey'})
            ], className='col-md-12 container-fluid mx-auto'),
            html.Div([
                "Date Range : ",
                dcc.DatePickerRange(
                    id='my-date-picker-range_graph4',
                    min_date_allowed=df_new['Posted Date'].min(),
                    max_date_allowed=df_new['Posted Date'].max(),
                    initial_visible_month=df_new['Posted Date'].max(),
                    start_date=df_new['Posted Date'].min(),
                    end_date=df_new['Posted Date'].max(),
                    className='dark-theme2'
                ),
            ], className='col-md-4', style={'padding-top': '10px', 'color': 'lightgrey'}),

            html.Div([
                "Brand Name: ",
                dcc.Dropdown(
                    id='brand_dropdown4',
                    options=[{'label': 'All', 'value': 'all'}] + brand_names,
                    value='all',
                    className='dark-theme',
                    placeholder="Select Brand"
                ),
            ], className='col-md-6', style={'color': 'lightgrey'}),

            # Bar chart of vehicle prices
            html.Div([
                dcc.Graph(id='vehicle-price-bar-chart-4')
            ]),
        ], className="g-3"),
    ], className='col-md-12'),

])


# first vehicle dropdown
@app.callback(
    dash.dependencies.Output('first_dropdown-2', 'options'),
    dash.dependencies.Input('first_dropdown-1', 'value'))
def update_second_dropdown2_options(selected_brand):
    if not selected_brand:
        return []
    models = df_new[df_new['Brand Name'] == selected_brand]['Model Name'].unique()
    options = [{'label': x, 'value': x} for x in models]
    return options


@app.callback(
    dash.dependencies.Output('first_dropdown-3', 'options'),
    dash.dependencies.Input('first_dropdown-2', 'value'))
def update_second_dropdown3_options(selected_brand):
    if not selected_brand:
        return []
    others = df_new[df_new['Model Name'] == selected_brand]['Other Name'].unique()
    options = [{'label': x, 'value': x} for x in others]
    return options


# second vehicle dropdown
@app.callback(
    dash.dependencies.Output('second_dropdown-2', 'options'),
    dash.dependencies.Input('second_dropdown-1', 'value'))
def update_second_dropdown2_options(selected_brand):
    if not selected_brand:
        return []
    models = df_new[df_new['Brand Name'] == selected_brand]['Model Name'].unique()
    options = [{'label': x, 'value': x} for x in models]
    return options


@app.callback(
    dash.dependencies.Output('second_dropdown-3', 'options'),
    dash.dependencies.Input('second_dropdown-2', 'value'))
def update_second_dropdown3_options(selected_brand):
    if not selected_brand:
        return []
    others = df_new[df_new['Model Name'] == selected_brand]['Other Name'].unique()
    options = [{'label': x, 'value': x} for x in others]
    return options


# third vehicle dropdown
@app.callback(
    dash.dependencies.Output('third_dropdown-2', 'options'),
    dash.dependencies.Input('third_dropdown-1', 'value'))
def update_third_dropdown2_options(selected_brand):
    if not selected_brand:
        return []
    models = df_new[df_new['Brand Name'] == selected_brand]['Model Name'].unique()
    options = [{'label': x, 'value': x} for x in models]
    return options


@app.callback(
    dash.dependencies.Output('third_dropdown-3', 'options'),
    dash.dependencies.Input('third_dropdown-2', 'value'))
def update_third_dropdown3_options(selected_brand):
    if not selected_brand:
        return []
    others = df_new[df_new['Model Name'] == selected_brand]['Other Name'].unique()
    options = [{'label': x, 'value': x} for x in others]
    return options


selected_vehicles = []

header_row = html.Tr([
    html.Th('Type of Vehicle'),
    html.Th('Brand Name'),
    html.Th('Model Name'),
    html.Th('Other Name')
])


@app.callback(
    dash.dependencies.Output('comparison-table', 'children'),
    [dash.dependencies.Input('first_add_button', 'n_clicks'),
     dash.dependencies.Input('clear_button', 'n_clicks')],
    [dash.dependencies.State('first_dropdown-1', 'value'),
     dash.dependencies.State('first_dropdown-2', 'value'),
     dash.dependencies.State('first_dropdown-3', 'value')]
)
def update_comparison_table(n_clicks, n_clicks2, first_dropdown1_value, first_dropdown2_value, first_dropdown3_value):
    global selected_vehicles

    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'first_add_button' and all(
                [first_dropdown1_value, first_dropdown2_value, first_dropdown3_value]):
            filtered_data = df_new[(df_new['Brand Name'] == first_dropdown1_value) &
                                   (df_new['Model Name'] == first_dropdown2_value) &
                                   (df_new['Other Name'] == first_dropdown3_value)]
            selected_vehicles.append(filtered_data)
        elif button_id == 'clear_button':
            selected_vehicles = []

    table_rows = [header_row]
    for vehicle in selected_vehicles:
        type1 = html.Td(vehicle['type_of_Vehicle'].iloc[0])
        brand = html.Td(vehicle['Brand Name'].iloc[0])
        model = html.Td(vehicle['Model Name'].iloc[0])
        other = html.Td(vehicle['Other Name'].iloc[0])
        table_rows.append(html.Tr([
            type1,
            brand,
            model,
            other
        ]))
    table = html.Table(table_rows)

    return table


@app.callback(
    dash.dependencies.Output('newly-added-vehicle', 'children'),
    dash.dependencies.Input('brand_dropdown2', 'value')
)
def update_vehicle_latest(brand):
    if brand == 'all':
        cards = [dbc.Card(

            dbc.CardBody([
                dbc.CardImg(src='/assets/Lovepik_com-401291116-new-label.png',
                            style={"width": "100px", "height": "100px"}),
                html.H5(f"{row['Brand Name']} ({row['Model Name']})", className="card-title mb-2 text-success"),
                html.Ul([
                    html.Li(f"Price: {row['price']}", className="card-text text-info"),
                    html.Li(f"Depreciation: {row['depreciation']}", className="card-text text-info"),
                    # Fix typo in column name
                    html.Li(f"Registration Date: {row['reg_Date']}", className="card-text text-info"),
                    html.Li(f"Engine Capacity: {row['engine_Cap']}", className="card-text text-info"),
                    html.Li(f"Mileage: {row['mileage']}", className="card-text text-info"),
                    # Fix typo in column name and lowercase km
                ], className="list-unstyled mb-3"),
                html.A(dbc.Button("Learn More", color="primary", className="btn-sm"), href=row['Vehicle Link']),
            ], className="p-3", style={'background-color': 'rgb(50, 50, 50)', 'border-radius': '10px',
                                       'border-color': 'rgb(50, 50, 50)'})
        ) for index, row in df_newly_added.iterrows()]

        return dbc.Row(cards, className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3")
    else:
        filtered_df = df_newly_added[(df_newly_added['Brand Name'] == brand)]
        cards = [dbc.Card(

            dbc.CardBody([
                dbc.CardImg(src='/assets/Lovepik_com-401291116-new-label.png',
                            style={"width": "100px", "height": "100px"}),
                html.H5(f"{row['Brand Name']} ({row['Model Name']})", className="card-title mb-2 text-success"),
                html.Ul([
                    html.Li(f"Price: {row['price']}", className="card-text text-info"),
                    html.Li(f"Depreciation: {row['depreciation']}", className="card-text text-info"),
                    # Fix typo in column name
                    html.Li(f"Registration Date: {row['reg_Date']}", className="card-text text-info"),
                    html.Li(f"Engine Capacity: {row['engine_Cap']}", className="card-text text-info"),
                    html.Li(f"Mileage: {row['mileage']}", className="card-text text-info"),
                    # Fix typo in column name and lowercase km
                ], className="list-unstyled mb-3"),
                html.A(dbc.Button("Learn More", color="primary", className="btn-sm"), href=row['Vehicle Link']),
            ], className="p-3", style={'background-color': 'rgb(50, 50, 50)', 'border-radius': '10px',
                                       'border-color': 'rgb(50, 50, 50)'})
        ) for index, row in filtered_df.iterrows()]

        return dbc.Row(cards, className="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-3")


@app.callback(
    dash.dependencies.Output('vehicle-price-bar-chart-3', 'figure'),
    [
        dash.dependencies.Input('brand_dropdown3', 'value'),
        dash.dependencies.Input('my-date-picker-range_graph3', 'start_date'),
        dash.dependencies.Input('my-date-picker-range_graph3', 'end_date'), ]
)
def update_vehicle_price_bar_chart2(brand, start_date, end_date):
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    filtered_df = df_new.loc[df_new['Posted Date'].between(*date_range)]

    if brand == 'all':
        avg_depreciation_by_type = filtered_df.groupby('type_of_Vehicle')['depreciation'].mean()
        fig = go.Figure(go.Bar(x=avg_depreciation_by_type.index, y=avg_depreciation_by_type.values,
                               text=avg_depreciation_by_type.values, textposition='auto'))
    else:
        filtered_df = df_new[(df_new['Brand Name'] == brand)]
        avg_depreciation_by_type = filtered_df.groupby('type_of_Vehicle')['depreciation'].mean()
        fig = go.Figure(go.Bar(x=avg_depreciation_by_type.index, y=avg_depreciation_by_type.values,
                               text=avg_depreciation_by_type.values, textposition='auto'))

    fig.update_layout(
        xaxis_title="Vehicle Type",
        yaxis_title="Average Depreciation ($)",
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
    dash.dependencies.Output('vehicle-price-bar-chart-4', 'figure'),
    [
        dash.dependencies.Input('brand_dropdown4', 'value'),
        dash.dependencies.Input('my-date-picker-range_graph4', 'start_date'),
        dash.dependencies.Input('my-date-picker-range_graph4', 'end_date'), ]
)
def update_vehicle_price_bar_chart2(brand, start_date, end_date):
    if start_date is None or end_date is None:
        return []
    date_range = [pd.to_datetime(start_date), pd.to_datetime(end_date)]
    filtered_df = df_new.loc[df_new['Posted Date'].between(*date_range)]

    if brand == 'all':
        avg_depreciation_by_type = filtered_df.groupby('type_of_Vehicle')['price'].mean()
        fig = go.Figure(go.Bar(x=avg_depreciation_by_type.index, y=avg_depreciation_by_type.values,
                               text=avg_depreciation_by_type.values, textposition='auto'))
    else:
        filtered_df = df_new[(df_new['Brand Name'] == brand)]
        avg_depreciation_by_type = filtered_df.groupby('type_of_Vehicle')['price'].mean()
        fig = go.Figure(go.Bar(x=avg_depreciation_by_type.index, y=avg_depreciation_by_type.values,
                               text=avg_depreciation_by_type.values, textposition='auto'))

    fig.update_layout(
        xaxis_title="Vehicle Type",
        yaxis_title="Average Price ($)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',

        margin=dict(l=20, r=20, t=20, b=20),
        template='plotly_white',
        autosize=True,
        font=dict(family="Arial, sans-serif", size=14, color="#7f7f7f"))

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    return fig
