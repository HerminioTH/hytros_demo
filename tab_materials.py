import dash_bootstrap_components as dbc
from dash import html, dcc

tab_materials = dcc.Tab(
        label="Material compatibility",
        value="mat-compat",
        children=[
            html.Br(),

            html.Div(
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            title="Short version",
                            children=[
                                html.P("This is the content of the first section"),
                            ],
                        ),
                        dbc.AccordionItem(
                            title="Extended version",
                            children=[
                                html.P("This is the content of the first section"),
                            ],
                        ),
                    ],
                    always_open=True,
                )
            )
        ]
    )
