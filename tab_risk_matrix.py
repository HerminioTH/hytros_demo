from dash import dcc, html, callback, Output, Input, MATCH, ALL
import plotly.express as px
import plotly.graph_objects as go
from utils import gid
import pandas as pd
import numpy as np

# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", hover_data=['petal_width', 'species_id'])


tab_risk_matrix = dcc.Tab(
        label="Risk matrix",
        value="tab-risk-matrix",
        children=[
            # html.Div(id="upload-status"),

            html.Br(),

            dcc.Graph(
                id="risk-matrix",
                # figure=fig,
                style={"height": "500px", "width": "700px"}
            ),
        ]
    )

@callback(
    Output(component_id="risk-matrix", component_property="figure"),
    Input(component_id=gid("well_design", "mitigation", ALL),  component_property="children"),
    Input(component_id={"tab": "well_design", "name": "impact", "i": ALL},  component_property="value"),
    Input(component_id=gid("well_integrity", "mitigation", ALL),  component_property="children"),
    Input(component_id={"tab": "well_integrity", "name": "impact", "i": ALL},  component_property="value"),
)
def build_dataframe(wd_mit, wd_impact, wi_mit, wi_impact):
    mitigation = wd_mit + wi_mit
    impact = wd_impact + wi_impact

    mitigation_dict = {
        "Severe": 4,
        "Moderate": 3,
        "Minor": 2,
        "No or minor": 1,
        "Unknown": 0,
        "": 0
    }
    impact_dict = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "": 0,
        None: 0
    }

    data_dict = {
        "Mitigation Label": mitigation,
        "Impact Label": impact,
        "Category": ["Well design" for i in range(len(wd_mit))] + ["Well element" for i in range(len(wi_mit))],
        "Category Number": [i+1 for i in range(len(wd_mit))] + [i+1 for i in range(len(wi_mit))],
        "Mitigation": [mitigation_dict[x] for x in mitigation],
        "Impact": [impact_dict[x] for x in impact],
    }

    df = pd.DataFrame(data_dict)

    df_count = df.groupby(["Mitigation", "Impact"]).size().reset_index(name="count")

    r = 0.12  # explosion radius in data units (tune)
    for line in df_count.values:
        mit, imp, _ = line
        ids = (df["Mitigation"] == mit) & (df["Impact"] == imp)

        n = len(df[ids].index)
        if n > 1:
            angles = np.linspace(0, 2*np.pi, n, endpoint=False)
            
            for ind, angle in zip(df[ids].index, angles):
                df.loc[ind, "Impact"] += r * np.cos(angle)
                df.loc[ind, "Mitigation"] += r * np.sin(angle)



    green_yellow_red = [
        [0.0, "#43c543"],
        [0.5, "#fff130"],
        [1.0, "#c02727"],
    ]

    fig = go.Figure(
        data=go.Heatmap(
            x=[1, 2, 3],
            y=[1, 2, 3, 4],
            z=[
                [0.0, 0.5, 0.7],
                [0.2, 0.6, 0.8],
                [0.4, 0.7, 0.9],
                [0.8, 0.9, 1.0],
            ],
            colorscale=green_yellow_red,
            showscale=False,
        )
    )
    scatter_fig = px.scatter(
                    df, 
                    x="Impact",
                    y="Mitigation",
                    color="Category",
                    hover_data=['Mitigation Label', 'Impact Label', 'Category Number']
    )
    fig.add_traces(
        scatter_fig.data
    )

    fig.update_traces(
        marker=dict(
            size=14,
            opacity=1.0,
            line=dict(
                color="black",   # edge color
                width=2          # edge thickness
            )  
        ),
        selector=dict(type="scatter")
    )

    fig.update_xaxes(
        range=[0.5, 3.5],
        tickmode="array",
        tickvals=[1, 2, 3],
        ticktext=["Low", "Medium", "High"],
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        range=[0.5, 4.5],
        tickmode="array",
        tickvals=[1, 2, 3, 4],
        ticktext=["No", "No or minor", "Moderate", "Severe"],
        showgrid=False,
        zeroline=False
    )

    fig.update_layout(
        plot_bgcolor="lightgray"   # inside the axes
    )

    return fig