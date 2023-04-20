import pandas as pd
import dash
from dash import html, dash_table, dcc
from app import app
import plotly.express as px

df_new = pd.read_csv('news.csv')

dropdown_options = [{'label': x, 'value': x} for x in df_new['Brand Name'].unique()]

layout = html.Div([
    html.Div([
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

    html.Div(children=[
        html.Div([
            html.Div([
                html.H5('Vehicle Comparison', className='text-center',
                        style={'color': 'lightgrey'})
            ], className='col-md-12 container-fluid mx-auto'),
            # First row
            html.Div([
                html.Div([
                    "Select a first vehicle"
                ], className='col-md-3'),
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-1', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Brand"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-2', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Model"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='first_dropdown-3', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Other Name"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
            ], className="row mt-3"),

            # Second row
            html.Div([
                html.Div([
                    "Select a second vehicle"
                ], className='col-md-3'),
                html.Div([

                    dcc.Dropdown(
                        id='second_dropdown-1', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Brand"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='second_dropdown-2', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Model"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='second_dropdown-3', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Other Name"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
            ], className="row mt-3"),

            # Third row
            html.Div([
                html.Div([
                    "Select a third vehicle"
                ], className='col-md-3'),
                html.Div([

                    dcc.Dropdown(
                        id='third_dropdown-1', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Brand"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='third_dropdown-2', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Model"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
                html.Div([

                    dcc.Dropdown(
                        id='third_dropdown-3', options=dropdown_options, value='',
                        className='dark-theme',
                        placeholder="Select Other Name"
                    ),
                ], className='col-md-3', style={'color': 'lightgrey'}),
            ], className="row mt-3"),
        ], className='col-md-12'),

        html.Div(id='comparison-table', style={'padding-top': '30px'})
    ], className='col-md-12')

])


# first vehicle dropdown
@app.callback(
    dash.dependencies.Output('first_dropdown-2', 'options'),
    dash.dependencies.Input('first_dropdown-1', 'value'))
def update_first_dropdown2_options(selected_brand):
    if not selected_brand:
        return []
    models = df_new[df_new['Brand Name'] == selected_brand]['Model Name'].unique()
    options = [{'label': x, 'value': x} for x in models]
    return options


@app.callback(
    dash.dependencies.Output('first_dropdown-3', 'options'),
    dash.dependencies.Input('first_dropdown-2', 'value'))
def update_first_dropdown3_options(selected_brand):
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


# Define the callback function to update the graph when the dropdowns are changed
@app.callback(
    dash.dependencies.Output('comparison-table', 'children'),
    [dash.dependencies.Input('first_dropdown-1', 'value'),
     dash.dependencies.Input('first_dropdown-2', 'value'),
     dash.dependencies.Input('first_dropdown-3', 'value'),
     dash.dependencies.Input('second_dropdown-1', 'value'),
     dash.dependencies.Input('second_dropdown-2', 'value'),
     dash.dependencies.Input('second_dropdown-3', 'value'),
     dash.dependencies.Input('third_dropdown-1', 'value'),
     dash.dependencies.Input('third_dropdown-2', 'value'),
     dash.dependencies.Input('third_dropdown-3', 'value')
     ])
def update_table(first_dropdown1_value, first_dropdown2_value, first_dropdown3_value, second_dropdown1_value,
                 second_dropdown2_value, second_dropdown3_value, third_dropdown1_value, third_dropdown2_value,
                 third_dropdown3_value):
    # Check that all dropdowns for both vehicles have been selected
    if not all([first_dropdown1_value, first_dropdown2_value, first_dropdown3_value,
                second_dropdown1_value, second_dropdown2_value, second_dropdown3_value, third_dropdown1_value,
                third_dropdown2_value,
                third_dropdown3_value]):
        return html.Div("Please select all dropdowns for both vehicles.")
    # Filter the data based on the selected brands
    filtered_data1 = df_new[(df_new['Brand Name'] == first_dropdown1_value) &
                            (df_new['Model Name'] == first_dropdown2_value) &
                            (df_new['Other Name'] == first_dropdown3_value)]
    filtered_data2 = df_new[(df_new['Brand Name'] == second_dropdown1_value) &
                            (df_new['Model Name'] == second_dropdown2_value) &
                            (df_new['Other Name'] == second_dropdown3_value)]
    filtered_data3 = df_new[(df_new['Brand Name'] == third_dropdown1_value) &
                            (df_new['Model Name'] == third_dropdown2_value) &
                            (df_new['Other Name'] == third_dropdown3_value)]

    # Create the comparison table
    table = html.Table([
        html.Tr([
            html.Th('Type of Vehicle'),
            html.Td(filtered_data1['type_of_Vehicle'].iloc[0]),
            html.Td(filtered_data2['type_of_Vehicle'].iloc[0]),
            html.Td(filtered_data3['type_of_Vehicle'].iloc[0])
        ]),
        html.Tr([
            html.Th('Brand Name'),
            html.Td(filtered_data1['Brand Name'].iloc[0]),
            html.Td(filtered_data2['Brand Name'].iloc[0]),
            html.Td(filtered_data3['Brand Name'].iloc[0])
        ]),
        html.Tr([
            html.Th('Model Name'),
            html.Td(filtered_data1['Model Name'].iloc[0]),
            html.Td(filtered_data2['Model Name'].iloc[0]),
            html.Td(filtered_data3['Model Name'].iloc[0])
        ]),
        html.Tr([
            html.Th('Other Name'),
            html.Td(filtered_data1['Other Name'].iloc[0]),
            html.Td(filtered_data2['Other Name'].iloc[0]),
            html.Td(filtered_data3['Other Name'].iloc[0])
        ]),
        html.Tr([
            html.Th('Price'),
            html.Td(filtered_data1['price'].iloc[0]),
            html.Td(filtered_data2['price'].iloc[0]),
            html.Td(filtered_data3['price'].iloc[0])
        ]),
        html.Tr([
            html.Th('Depreciation'),
            html.Td(filtered_data1['depreciation'].iloc[0]),
            html.Td(filtered_data2['depreciation'].iloc[0]),
            html.Td(filtered_data3['depreciation'].iloc[0])
        ]),
        html.Tr([
            html.Th('Reg Date'),
            html.Td(filtered_data1['reg_Date'].iloc[0]),
            html.Td(filtered_data2['reg_Date'].iloc[0]),
            html.Td(filtered_data3['reg_Date'].iloc[0])
        ]),
        html.Tr([
            html.Th('Mileage'),
            html.Td(filtered_data1['mileage'].iloc[0]),
            html.Td(filtered_data2['mileage'].iloc[0]),
            html.Td(filtered_data3['mileage'].iloc[0])
        ]),
        html.Tr([
            html.Th('Road Tax'),
            html.Td(filtered_data1['road_Tax'].iloc[0]),
            html.Td(filtered_data2['road_Tax'].iloc[0]),
            html.Td(filtered_data3['road_Tax'].iloc[0])
        ]),
        html.Tr([
            html.Th('Dereg Value'),
            html.Td(filtered_data1['dereg_Value'].iloc[0]),
            html.Td(filtered_data2['dereg_Value'].iloc[0]),
            html.Td(filtered_data3['dereg_Value'].iloc[0])
        ]),
        html.Tr([
            html.Th('COE'),
            html.Td(filtered_data1['COE'].iloc[0]),
            html.Td(filtered_data2['COE'].iloc[0]),
            html.Td(filtered_data3['COE'].iloc[0])
        ]),
        html.Tr([
            html.Th('Engine Cap'),
            html.Td(filtered_data1['engine_Cap'].iloc[0]),
            html.Td(filtered_data2['engine_Cap'].iloc[0]),
            html.Td(filtered_data3['engine_Cap'].iloc[0])
        ]),
        html.Tr([
            html.Th('Curb Weight'),
            html.Td(filtered_data1['curb_Weight'].iloc[0]),
            html.Td(filtered_data2['curb_Weight'].iloc[0]),
            html.Td(filtered_data3['curb_Weight'].iloc[0])
        ]),
        html.Tr([
            html.Th('Transmission'),
            html.Td(filtered_data1['transmission'].iloc[0]),
            html.Td(filtered_data2['transmission'].iloc[0]),
            html.Td(filtered_data3['transmission'].iloc[0])
        ]),
        html.Tr([
            html.Th('OMV'),
            html.Td(filtered_data1['OMV'].iloc[0]),
            html.Td(filtered_data2['OMV'].iloc[0]),
            html.Td(filtered_data3['OMV'].iloc[0])
        ]),
        html.Tr([
            html.Th('ARF'),
            html.Td(filtered_data1['ARF'].iloc[0]),
            html.Td(filtered_data2['ARF'].iloc[0]),
            html.Td(filtered_data3['ARF'].iloc[0])
        ]),
        html.Tr([
            html.Th('Fuel Type'),
            html.Td(filtered_data1['fuel_Type'].iloc[0]),
            html.Td(filtered_data2['fuel_Type'].iloc[0]),
            html.Td(filtered_data3['fuel_Type'].iloc[0])
        ])
    ])

    return table
