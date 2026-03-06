from dash import dcc, html, callback, Output, Input, MATCH, ALL
import plotly.express as px
import plotly.graph_objects as go
from utils import gid
import pandas as pd
import numpy as np


# tab_risk_matrix = dcc.Tab(
#     label="Results",
#     value="tab-risk-matrix",
#     children=[
#         html.Br(),
#         dcc.Graph(
#             id="risk-matrix",
#             # figure=fig,
#             style={"height": "500px", "width": "700px"}
#         ),
#     ]
# )

cw_1 = 20
cw_2 = 80

def set_style(width, textAlign="left", bold=None, fontsize=24):
    style = {
        "textAlign": textAlign,
        "verticalAlign": "middle",
        "padding": "10px 10px",        # ← controls space inside cells
        "fontWeight": bold,
        "fontSize": fontsize,
        "width": str(width)+"%",
        "borderRadius": "5px",
        "backgroundColor": "white"
    }
    return style

def create_criteria_table():
    style_0 = {
        "width": "1px"
    }
    def get_style(bg_color="#FFFFFF", txt_color="#000000"):
        style_1 = {
            "textAlign": "right",
            "padding": "10px 5px",
            "width": "1px",
            "fontWeight": "bold",
            "backgroundColor": bg_color,
            "color": txt_color,
        }
        return style_1
    style_2 = {
        "padding": "10px 20px",
        "width": "20px",
        "fontWeight": "normal"
    }
    table = html.Table(
        [
            html.Tbody([
                # html.Tr([
                #     html.Td("", style=style_0),
                #     html.Td("Mitigation", style=get_style()),
                #     html.Td("Defines the level of additional work that is required to remediate the assessed element. ", style=style_2),
                # ]),
                html.Tr([
                    html.Td("", style=style_0),
                    # html.Td("No or minor", style={"width": "5px", "backgroundColor": "#c02727", "fontWeight": "bold", "textAlign": "right"}),
                    html.Td("No or minor", style=get_style("#43c543", "#000000")),
                    html.Td("No remediations and well operations are required; only some additional engineering " \
                    "review work could be expected for the well in its current state e.g. processing and analysis on data. ", style=style_2),
                ]),
                html.Tr([
                    html.Td("", style=style_0),
                    html.Td("Moderate", style=get_style("#fff130", "#000000")),
                    html.Td("Remediation, additional assessment and verification or risk management strategy could " \
                    "be expected. This could include detailed engineering assessment, techno-economical analysis and/or interventions that " \
                    "are typically done on retrievable components. ", style=style_2),
                ]),
                html.Tr([
                    html.Td("", style=style_0),
                    html.Td("Severe", style=get_style("#c02727", "#FFFFFF")),
                    html.Td("Remediation and a comprehensive risk management strategy could be expected. This typically " \
                    "involves technically challenging operations on non-retrievable components. ", style=style_2),
                ]),
                html.Tr([
                    html.Td("", style=style_0),
                    html.Td("Unknown", style=get_style("#4E4E4E", "#FFFFFF")),
                    html.Td("Critical information is missing for assessment with the screening tool. It is advised to look for additional data, " \
                    "acquire additional data (e.g. by running logs) or look for offset data, and then reassess the well with the " \
                    "screening tool.", style=style_2),
                ]),
            ])
        ],
        style={"width": "100%", "border": "1px solid #999"}
        # style={"width": "700px", "border": "1px solid #999"}
    )
    return table

tab_risk_matrix = dcc.Tab(
    label="Results",
    value="tab-risk-matrix",
    children=[
        html.Br(),
        
        html.Div(
            style={"width": "100%", "margin": "16px auto", "fontFamily": "system-ui", "textAlign": "center"},
            children=[
                html.Table(
                    children=[
                        html.Thead(
                            html.Tr([
                                html.Th("Risk matrix", style=set_style(cw_1, textAlign="center")),
                                html.Th("Criteria", style=set_style(cw_2, textAlign="center")),
                            ])
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(
                                    [
                                        dcc.Graph(
                                            id="risk-matrix",
                                            style={"height": "500px", "width": "700px", "verticalAlign": "top"}
                                        ),
                                    ],
                                    style={"verticalAlign": "top"}
                                ),
                                html.Td(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.Br(),
                                        html.Br(),
                                        html.Img(
                                            src="/assets/mitigation_impact.png",  # put image inside assets folder
                                            style={"width": "70%", "height": "auto", "textAlign": "right"}
                                        ),
                                    ],
                                    style={"verticalAlign": "top"}),
                            ])
                        ]),
                    ],
                    style={
                        "width": "100%",
                    }
                )
            ]
        )
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
        # title="Risk Matrix",
        # title_x=0.5,
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