import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc

# Connect to main app.py file
from app import app
from app import server

from apps import home, latest_vehicles

navbar = html.Div(
    [
        html.Div([
            html.Div([
                html.Img(src="/assets/statistics.png", style={"width": "4.9rem"}),
                html.H5("Vehicle Data Analyzer", style={'color': 'white', 'margin-top': '20px'}),
            ], className='image_title')
        ], className="sidebar-header"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink([html.Div([
                    html.I(className="fa-solid fa-house"),
                    html.Span("Home", style={'margin-top': '3px', 'padding-left': '10px'})], className='icon_title')],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink([html.Div([
                    html.I(className="fa-solid fa-gauge"),
                    html.Span("Newest Vehicles", style={'margin-top': '3px', 'padding-left': '10px'})],
                    className='icon_title')],
                    href="/apps/latest_vehicles",
                    active="exact",
                    className="pe-3"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="bg_id",
    className="sidebar",
)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    navbar,
    html.Div(id="page-content")
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/apps/latest_vehicles":
        return latest_vehicles.layout
    else:
        return html.P("404 - Page not found")


if __name__ == '__main__':
    app.run_server(debug=True)
