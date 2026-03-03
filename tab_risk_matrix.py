from dash import dcc, html, callback, Output, Input, MATCH, ALL
import plotly.express as px
import plotly.graph_objects as go
from utils import gid
import pandas as pd
import numpy as np


tab_risk_matrix = dcc.Tab(
        label="Results",
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
    Input(component_id=gid("well_integrity", "mitigation", ALL),  component_property="children"),
    Input(component_id={"tab": "well_integrity", "name": "impact", "i": ALL},  component_property="value"),
)
def build_dataframe(wi_mit, wi_impact):
    mitigation = wi_mit
    impact = wi_impact

    mitigation_dict = {
        "Severe": 3,
        "Moderate": 2,
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
        "Category": ["Well Integrity" for i in range(len(wi_mit))],
        "Category Number": [i+1 for i in range(len(wi_mit))],
        "Mitigation": [mitigation_dict[x] for x in mitigation],
        "Impact": [impact_dict[x] for x in impact],
        "Questions": [
            "1. Primary caprock",
            "2. Production casing/liner",
            "3. Cement behind the production casing/liner",
            "4. Overlapping casing behing the production casing/liner",
            "5. Cement behind the overlapping casing",
            "6. Secondary caprock",
            "7. Casing string across the secondary caprock",
            "8. Cement behind the casing string...",
            "9. Overlapping casing behind the production casing/liner",
            "10. Cement behind the overlapping casing",
            "11. Wellhead",
            "12. Other non-retrievable completion e.g. sand screens",
            "13. Production packer",
            "14. SSSV",
            "15. Tubing",
            "16. X-mas tree and valves",
            "17. Wellhead casing spools and hangers",
            "18. Any other completion..."

        ]
    }

    df = pd.DataFrame(data_dict)
    print(df)

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
        [0.0, "#35b335"],
        [0.5, "#fff130"],
        [1.0, "#c02727"],
    ]

    fig = go.Figure(
        data=go.Heatmap(
            x=[1, 2, 3],
            y=[1, 2, 3],
            z=[
                [0.0, 0.0, 0.0],
                [0.0, 0.5, 0.5],
                [0.0, 0.5, 1.0],
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
                    hover_data=['Questions']
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
        range=[-0.5, 3.5],
        tickmode="array",
        tickvals=[0, 1, 2, 3],
        ticktext=["Unknown", "Low", "Medium", "High"],
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        range=[-0.5, 3.5],
        tickmode="array",
        tickvals=[0, 1, 2, 3],
        ticktext=["Unknown", "No or minor", "Moderate", "Severe"],
        showgrid=False,
        zeroline=False
    )

    fig.update_layout(
        plot_bgcolor="lightgray",   # inside the axes
        title="Risk Matrix",
        title_x=0.5,
        xaxis=dict(
            title=dict(
                text="Impact",
                font=dict(size=16)
            )
        ),
        yaxis=dict(
            title=dict(
                text="Mitigation",
                font=dict(size=16)
            )
        ),
        # showlegend=False
    )

    return fig