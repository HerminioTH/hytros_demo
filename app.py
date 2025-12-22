from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
import pandas as pd
import json

app = Dash(__name__)
app.title = "HyTROS"

server = app.server

df = pd.DataFrame([
    {
        "#": 1,
        "Criteria category": "Status",
        "Criteria sub-category": "Is the well accessible?",
        "Full question": "Is the well accessible?",
        "Answer": "Yes",
        "Mitigation": "No or minor",
        "Impact": "High"
    },
    {
        "#": 2,
        "Criteria category": "Age",
        "Criteria sub-category": "Is the well constructed before 1996?",
        "Full question": "Is the well constructed before 1996?",
        "Answer": "Yes",
        "Mitigation": "Moderate",
        "Impact": "Low"
    },
    {
        "#": 3,
        "Criteria category": "Type / function",
        "Criteria sub-category": "Was the well used as injector?",
        "Full question": "Was the well used as injector e.g. brine for pressure maintenance?",
        "Answer": "No",
        "Mitigation": "Severe",
        "Impact": "Low"
    },
    {
        "#": 4,
        "Criteria category": "Depth",
        "Criteria sub-category": "Are the depth intervals adequate?",
        "Full question": "Is change in target depth required? For example, drilling or sidetracking to reach deeper zones, or perforating, milling shallower intervals.",
        "Answer": "Yes",
        "Mitigation": "Severe",
        "Impact": "High"
    },
    {
        "#": 5,
        "Criteria category": "Diameter",
        "Criteria sub-category": "Is diameter sufficient for operations?",
        "Full question": "Is the well diameter sufficient for the expected operational conditions and performance?",
        "Answer": "Yes",
        "Mitigation": "No or minor",
        "Impact": "High"
    },
    {
        "#": 6,
        "Criteria category": "Deviation",
        "Criteria sub-category": "Inclination across caprock(s) > 30°?",
        "Full question": "Is the inclination of the well across the caprock(s) higher than 30 degrees?",
        "Answer": "No",
        "Mitigation": "unknown",
        "Impact": "Medium"
    },
    {
        "#": 7,
        "Criteria category": "Geological and geomechanical occurances",
        "Criteria sub-category": "Any mechanisms affecting integrity?",
        "Full question": "Are there indication of geological or geomehcanical mechanisms (e.g. tectonic forces, presence of fractures and faults etc) that could affect well components related to structural integrity i.e. wellhead, conductor casing?",
        "Answer": "Unknown",
        "Mitigation": "unknown",
        "Impact": "Medium"
    },
    {
        "#": 8,
        "Criteria category": "Operational issues",
        "Criteria sub-category": "Any integrity issues (SCP/leakage)?",
        "Full question": "Has the well experienced any integrity issues, such as sustained casing pressure (SCP) or leakage in any relevant annulus?",
        "Answer": "Yes",
        "Mitigation": "Moderate",
        "Impact": "Medium"
    },
])
# df = df[["#", "Criteria category", "Criteria sub-category", "Answer", "Mitigation", "Impact"]]
# df["Criteria sub-category"] = df["Full question"]

ANSWER_OPTIONS = [{"label": v, "value": v} for v in ["Yes", "No", "Unknown"]]

# ---------- Layout ----------
app.layout = html.Div(
    style={"maxWidth": "1500px", "margin": "24px auto", "fontFamily": "system-ui"},
    children=[
        html.H2("HyTROS Screening Framework"),

        # Shared state between tabs
        dcc.Store(id="app-state", storage_type="memory"),

        dcc.Tabs(
            id="tabs",
            value="tab-design",
            children=[
                dcc.Tab(
                    label="Instructions",
                    value="tab-how",
                    children=[
                        dcc.Markdown("""
                            The screening is conducted through two screening categories:

                            1) Well design  - pre screening, focusing on the design and operational aspects.

                            2) Well integrity - detailed screening of well integrity barrier elements.
                             
                            For each category, a set of qualitative criteria (questions) are defined, 
                            answered with yes, no or unknown. For Well Integrity, answers to criteria questions 
                            will reflect whether WBE is "Qualified / FFS" and have "Material compatibility". 
                            For latter, please refer to the material compatibility sheet. For non-retrievable WBEs, 
                            both Qualified / FFS and Material compatibility have to be positive. Otherwise, 
                            mitigation will be severe. For retrievable WBEs, if both Qualified / FFS and Material 
                            compatibility are not positive, mitigation will be moderate. 

                            User then selects the level of impact based on the consequences on the operation. Please refer to the Criteria sheet for further details. 

                            Screening results are represented through:
                            Mitigation requirements – hard-coded based on criteria questions
                            Impact – user selected
                        """)
                    ],
                ),

                dcc.Tab(
                    label = "Well Design",
                    value = "tab-design",
                    children = [
                        html.Div(
                            style={"maxWidth": "1500px", "margin": "16px auto", "fontFamily": "system-ui"},
                            children=[
                                dash_table.DataTable(
                                    id="criteria-table",
                                    data=df.to_dict("records"),
                                    columns=[
                                        {"name": "#", "id": "#", "type": "numeric"},
                                        {"name": "Criteria category", "id": "Criteria category"},
                                        {"name": "Criteria sub-category", "id": "Criteria sub-category"},
                                        {"name": "Answer", "id": "Answer", "presentation": "dropdown"},
                                        {"name": "Mitigation", "id": "Mitigation"},
                                        {"name": "Impact", "id": "Impact"},
                                    ],
                                    editable=True,
                                    dropdown={
                                        "Answer": {"options": ANSWER_OPTIONS}
                                    },

                                    # Layout/UX like Excel
                                    style_table={"overflowX": "auto"},
                                    style_header={"fontWeight": "700", "backgroundColor": "#f2f2f2"},
                                    style_cell={
                                        "padding": "5px",
                                        "whiteSpace": "normal",
                                        "height": "auto",
                                        "textAlign": "left",
                                        "border": "0px solid #ddd",
                                        "fontSize": "14px",
                                    },
                                    style_cell_conditional=[
                                        {"if": {"column_id": "#"}, "width": "50px", "textAlign": "center"},
                                        {"if": {"column_id": "Criteria category"}, "width": "260px"},
                                        {"if": {"column_id": "Criteria sub-category"}, "width": "780px"},
                                        {"if": {"column_id": "Answer"}, "width": "120px"},
                                        {"if": {"column_id": "Mitigation"}, "width": "160px", "fontWeight": "600"},
                                        {"if": {"column_id": "Impact"}, "width": "120px", "fontWeight": "600"},
                                    ],

                                    # Color-coded cells (Mitigation + Impact)
                                    style_data_conditional=[
                                        # Mitigation colors
                                        {"if": {"column_id": "Mitigation", "filter_query": '{Mitigation} = "No or minor"'},
                                         "backgroundColor": "#2e7d32", "color": "white"},
                                        {"if": {"column_id": "Mitigation", "filter_query": '{Mitigation} = "Moderate"'},
                                         "backgroundColor": "#ffeb3b", "color": "black"},
                                        {"if": {"column_id": "Mitigation", "filter_query": '{Mitigation} = "Severe"'},
                                         "backgroundColor": "#e53935", "color": "white"},
                                        {"if": {"column_id": "Mitigation", "filter_query": '{Mitigation} = "unknown"'},
                                         "backgroundColor": "#9e9e9e", "color": "black"},

                                        # Impact colors
                                        {"if": {"column_id": "Impact", "filter_query": '{Impact} = "Low"'},
                                         "backgroundColor": "#dff3d8", "color": "black"},
                                        {"if": {"column_id": "Impact", "filter_query": '{Impact} = "Medium"'},
                                         "backgroundColor": "#fff59d", "color": "black"},
                                        {"if": {"column_id": "Impact", "filter_query": '{Impact} = "High"'},
                                         "backgroundColor": "#f8d7c9", "color": "black"},
                                    ],
                                )
                            ],
                        )
                    ]
                ),

                dcc.Tab(
                    label = "Well Integrity",
                    value = "tab-integrity",
                    children = [
                        html.Div(
                            style = {
                                "padding": "30px",
                                # "gap": "120px",
                                # "alignItems": "left",
                            },
                            children = [
                                html.Label("#1 [Status]. Is the well accessible? "),
                                dcc.Dropdown(
                                    id="1-status",
                                    options=[
                                        {"label": "Yes", "value": "yes"},
                                        {"label": "No", "value": "no"},
                                        {"label": "Unknown", "value": "unknown"},
                                    ],
                                    # value="apples",
                                    clearable=True,
                                ),
                                html.Br(),

                                html.Label("#2 [Age]. Is the well accessible? "),
                                dcc.Dropdown(
                                    id="2-Age",
                                    options=[
                                        {"label": "Yes", "value": "yes"},
                                        {"label": "No", "value": "no"},
                                        {"label": "Unknown", "value": "unknown"},
                                    ],
                                    # value="apples",
                                    clearable=True,
                                ),
                                html.Br(),

                                html.Label("#3 [Type/Function]. Was the well used as injector e.g. brine for pressure maintenance? "),
                                dcc.Dropdown(
                                    id="3-type",
                                    options=[
                                        {"label": "Yes", "value": "yes"},
                                        {"label": "No", "value": "no"},
                                        {"label": "Unknown", "value": "unknown"},
                                    ],
                                    # value="apples",
                                    clearable=True,
                                ),
                                html.Br(),

                                html.Label("#4 [Depth]. Is chage in target depth required? For example, drilling or sidetracking to reach deeper zones, or perforating, milling shallower intervals. "),
                                dcc.Dropdown(
                                    id="4-depth",
                                    options=[
                                        {"label": "Yes", "value": "yes"},
                                        {"label": "No", "value": "no"},
                                        {"label": "Unknown", "value": "unknown"},
                                    ],
                                    # value="apples",
                                    clearable=True,
                                ),
                                html.Br(),
                            ]
                        )
                    ]
                ),


                dcc.Tab(
                    label="Dummy tab 1",
                    value="tab-inputs",
                    children=[
                        html.Div(
                            style={"padding": "16px"},
                            children=[
                                html.Label("Pick a dataset"),
                                dcc.Dropdown(
                                    id="dataset",
                                    options=[
                                        {"label": "Apples", "value": "apples"},
                                        {"label": "Oranges", "value": "oranges"},
                                        {"label": "Bananas", "value": "bananas"},
                                    ],
                                    value="apples",
                                    clearable=True,
                                ),
                                html.Br(),

                                html.Label("Choose processing steps"),
                                dcc.Checklist(
                                    id="steps",
                                    options=[
                                        {"label": "Normalize", "value": "normalize"},
                                        {"label": "Filter outliers", "value": "outliers"},
                                        {"label": "Log-transform", "value": "log"},
                                    ],
                                    value=["outliers"],
                                ),
                                html.Br(),

                                html.Label("Threshold"),
                                dcc.Slider(
                                    id="threshold",
                                    min=0,
                                    max=100,
                                    step=5,
                                    value=50,
                                    marks={0: "0", 50: "50", 100: "100"},
                                ),
                                html.Br(),

                                html.Label("Run name   \t"),
                                html.Br(),
                                dcc.Input(
                                    id="run-name",
                                    type="text",
                                    value="test_run",
                                    debounce=True,  # only fires when user leaves field / presses enter
                                    style={"width": "260px"},
                                ),
                                html.Br(),
                                html.Br(),

                                html.Button("Save selections", id="save-btn", n_clicks=0),

                                html.Div(
                                    id="save-status",
                                    style={"marginTop": "12px", "color": "#444"},
                                ),

                                html.Hr(),
                                html.Div(
                                    style={"color": "#666"},
                                    children=[
                                        "Tip: go to tab 2 to see how these selections are used."
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                dcc.Tab(
                    label="Dummy tab 2",
                    value="tab-results",
                    children=[
                        html.Div(
                            style={"padding": "16px"},
                            children=[
                                html.H4("Computed output from Tab 1 selections"),
                                html.Div(id="results-summary"),
                                html.Br(),
                                html.Pre(
                                    id="results-json",
                                    style={
                                        "background": "#f6f6f6",
                                        "padding": "12px",
                                        "borderRadius": "8px",
                                        "overflowX": "auto",
                                    },
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)

# ---------- Callbacks ----------
@callback(
    Output("app-state", "data"),
    Output("save-status", "children"),
    Input("save-btn", "n_clicks"),
    State("dataset", "value"),
    State("steps", "value"),
    State("threshold", "value"),
    State("run-name", "value"),
    prevent_initial_call=True,
)
def save_state(n_clicks, dataset, steps, threshold, run_name):
    data = {
        "dataset": dataset,
        "steps": steps,
        "threshold": threshold,
        "run_name": run_name,
    }
    print(data)
    return data, f"Saved! ({n_clicks} time(s))"


@callback(
    Output("results-summary", "children"),
    Output("results-json", "children"),
    Input("app-state", "data"),
)
def compute_results(data):
    if not data:
        return (
            html.Div("Nothing saved yet. Go to Tab 1 and click “Save selections”."),
            "",
        )

    # "Do something": compute a toy score based on chosen settings
    step_weight = {"normalize": 1.0, "outliers": 1.5, "log": 2.0}
    score = sum(step_weight.get(s, 0.0) for s in data["steps"]) * (data["threshold"] / 100.0)

    summary = html.Ul(
        children=[
            html.Li(f"Run name: {data['run_name']}"),
            html.Li(f"Dataset: {data['dataset']}"),
            html.Li(f"Steps: {', '.join(data['steps']) if data['steps'] else '(none)'}"),
            html.Li(f"Threshold: {data['threshold']}"),
            html.Li(f"Computed score: {score:.3f}"),
        ]
    )

    return summary, json.dumps({"inputs": data, "computed_score": score}, indent=2)


if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_hot_reload_interval=1000,  # ms between file checks
    )
