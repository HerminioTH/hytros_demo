from dash import dcc, html, callback, Output, Input, MATCH, ALL
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", hover_data=['petal_width', 'species_id'])


tab_risk_matrix = dcc.Tab(
        label="Risk matrix",
        value="tab-risk-matrix",
        children=[
            # html.Div(id="upload-status"),

            html.Br(),

            dcc.Graph(
                figure=fig,
                style={"height": "500px", "width": "700px"}
            ),
        ]
    )

@callback(
    Input(component_id="1-mitigation",  component_property="children"),
    Input(component_id="2-mitigation",  component_property="children"),
    Input(component_id="3-mitigation",  component_property="children"),
    Input(component_id="4-mitigation",  component_property="children"),
    Input(component_id="5-mitigation",  component_property="children"),
    Input(component_id="6-mitigation",  component_property="children"),
    Input(component_id="7-mitigation",  component_property="children"),
    Input(component_id="8-mitigation",  component_property="children"),
    Input(component_id={"tab": "well_design", "name": "impact", "i": ALL},  component_property="value"),
    
    Input(component_id="mit-1",  component_property="children"),
    Input(component_id="mit-2",  component_property="children"),
    Input(component_id="mit-3",  component_property="children"),
    Input(component_id="mit-4",  component_property="children"),
    Input(component_id="mit-5",  component_property="children"),
    Input(component_id="mit-6",  component_property="children"),
    Input(component_id="mit-7",  component_property="children"),
    Input(component_id="mit-8",  component_property="children"),
    Input(component_id="mit-9",  component_property="children"),
    Input(component_id="mit-10",  component_property="children"),
    Input(component_id="mit-11",  component_property="children"),
    Input(component_id="mit-12",  component_property="children"),
    Input(component_id="mit-13",  component_property="children"),
    Input(component_id="mit-14",  component_property="children"),
    Input(component_id="mit-15",  component_property="children"),
    Input(component_id="mit-16",  component_property="children"),
    Input(component_id="mit-17",  component_property="children"),
    Input(component_id="mit-18",  component_property="children"),
    Input(component_id={"tab": "well_integrity", "name": "impact", "i": ALL},  component_property="value"),
)
def build_dataframe(
            wd_mit_1,
            wd_mit_2,
            wd_mit_3,
            wd_mit_4,
            wd_mit_5,
            wd_mit_6,
            wd_mit_7,
            wd_mit_8,
            wd_impact,

            wi_mit_1,
            wi_mit_2,
            wi_mit_3,
            wi_mit_4,
            wi_mit_5,
            wi_mit_6,
            wi_mit_7,
            wi_mit_8,
            wi_mit_9,
            wi_mit_10,
            wi_mit_11,
            wi_mit_12,
            wi_mit_13,
            wi_mit_14,
            wi_mit_15,
            wi_mit_16,
            wi_mit_17,
            wi_mit_18,
            wi_impact,
            ):
    wd_mit = [wd_mit_1, wd_mit_2, wd_mit_3, wd_mit_4, wd_mit_5, wd_mit_6, wd_mit_7, wd_mit_8]
    wi_mit = [wi_mit_1, wi_mit_2, wi_mit_3, wi_mit_4, wi_mit_5, wi_mit_6, wi_mit_7, wi_mit_8,
              wi_mit_9, wi_mit_10, wi_mit_11, wi_mit_12, wi_mit_13, wi_mit_14, wi_mit_15, wi_mit_16, wi_mit_17, wi_mit_18]
    mitigation = wd_mit + wi_mit
    impact = wd_impact + wi_impact
    # print(wd_mit)
    # print(wd_impact)
    print()
    print("mitigation", mitigation)
    print("impact", impact)

    return