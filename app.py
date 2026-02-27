from dash import Dash, html, dcc, callback, Output, Input, State, ALL, no_update
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from tab_well_design import tab_well_design
from tab_instructions import tab_instructions
from tab_well_integrity import tab_well_integrity
from tab_risk_matrix import tab_risk_matrix
from tab_materials import tab_materials
import json
import base64

FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)
# external_stylesheets = [dbc.themes.BOOTSTRAP, FONT_AWESOME]
# external_stylesheets = [dbc.themes.SKETCHY, FONT_AWESOME]
external_stylesheets = [dbc.themes.FLATLY, FONT_AWESOME]

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


# ---------- Layout ----------
app.layout = html.Div(
    style={"maxWidth": "1500px", "margin": "24px auto", "fontFamily": "system-ui"},
    children=[
        html.H2("HyTROS Screening Framework"),

        # Shared state between tabs
        dcc.Store(id="app-state", storage_type="memory", data={}),

        dbc.Stack(
            direction="horizontal",
            gap=4,
            children=[
                dbc.Button(id="btn-download-json",
                    children=[html.I(className="fa fa-download me-2"), "Save well"],
                    color="primary",
                    className="mt-0"
                ),

                dcc.Upload(
                    id="upload-json",
                    multiple=False,
                    children=[
                        dbc.Button(id="btn-upload-json",
                            children=[html.I(className="fa fa-upload me-2"), "Load well"],
                            color="success",
                            className="mt-0"
                        ),
                    ]
                ),

                # dbc.Button(id="btn-apply",
                #     children=[html.I(className="fa fa-play me-2"), "Apply"],
                #     color="success",
                #     className="mt-0"
                # ),

                html.Div(id="upload-status"),
            ]
        ),

        dcc.Download(id="download-json"),

        html.H2(" "),

        dcc.Tabs(
            id="tabs",
            value="tab-how",
            # value="mat-compat",
            children=[
                tab_instructions,
                tab_well_design,
                tab_well_integrity,
                tab_risk_matrix,
                tab_materials
            ],
            style={
                "display": "flex",
                "height": "50px",
                "alignItems": "center", 
            }
        )
    ]
)



@callback(
    Output("download-json", "data"),
    Input("btn-download-json", "n_clicks"),
    State({"tab": "well_design", "name": ALL}, "value"),
    State({"tab": "well_design", "name": ALL}, "id"),
    State({"tab": "well_design", "name": "impact", "i": ALL}, "value"),
    State({"tab": "well_integrity", "question": ALL}, "value"),
    State({"tab": "well_integrity", "question": ALL}, "id"),
    State({"tab": "well_integrity", "name": "impact", "i": ALL}, "value"),
    State({"tab": "well_integrity", "barrier": ALL}, "id"),
    State({"tab": "well_integrity", "barrier": ALL}, "value"),
    State({"tab": "well_integrity", "retrievable": ALL}, "id"),
    State({"tab": "well_integrity", "retrievable": ALL}, "value"),
    prevent_initial_call=True,
)
def download_json(_, 
                  wdq_values,
                  wdq_ids,
                  wdi_values,
                  wiq_values,
                  wiq_ids,
                  wii_values,
                  wib_ids,
                  wib_values,
                  wir_ids,
                  wir_values,
    ):
    '''
    wdq - well_design_question
    wdi - well_design_impact
    wiq - well_integrity_question
    wii - well_integrity_impact
    '''
    data_dict = {"well_design": {}, "well_integrity": {}}

    for question, value, impact in zip(wdq_ids, wdq_values, wdi_values):
        data_dict["well_design"][question["name"]] = {"answer": value, "impact": impact}

    data_dict["well_integrity"]["questions"] = {}
    for question_id, question_value in zip(wiq_ids, wiq_values):
        data_dict["well_integrity"]["questions"][question_id["question"]] = question_value

    data_dict["well_integrity"]["barriers"] = {}
    for barrier_id, barrier_value in zip(wib_ids, wib_values):
        data_dict["well_integrity"]["barriers"][barrier_id["barrier"]] = barrier_value
        
    data_dict["well_integrity"]["retrievable"] = {}
    for ret_id, ret_value in zip(wir_ids, wir_values):
        data_dict["well_integrity"]["retrievable"][ret_id["retrievable"]] = ret_value

    data_dict["well_integrity"]["impact"] = {}
    for i, impact in enumerate(wii_values):
        data_dict["well_integrity"]["impact"][f"impact-{i+1}"] = impact

    content = json.dumps(data_dict, indent=4, ensure_ascii=False)
    return {
        "content": content,
        "filename": "app_data.json"
    }

@callback(
    Output("upload-status", "children"),
    Output({"tab": "well_design", "name": ALL}, "value"),
    Output({"tab": "well_design", "name": "impact", "i": ALL}, "value"),
    Output({"tab": "well_integrity", "barrier": ALL}, "value"),
    Output({"tab": "well_integrity", "retrievable": ALL}, "value"),
    Output({"tab": "well_integrity", "question": ALL}, "value"),
    Output({"tab": "well_integrity", "name": "impact", "i": ALL}, "value"),
    Input("upload-json", "contents"),
    State("upload-json", "filename"),
    prevent_initial_call=True,
)
def handle_upload(contents, filename):
    if not contents:
        raise PreventUpdate

    # contents is like: "data:application/json;base64,AAAA..."
    try:
        content_type, content_string = contents.split(",", 1)
        decoded_bytes = base64.b64decode(content_string)
        decoded_text = decoded_bytes.decode("utf-8")

        data = json.loads(decoded_text)  # <-- your dict
        
        answers, wd_impacts = [], []
        for value in data["well_design"].values():
            answers.append(value["answer"])
            wd_impacts.append(value["impact"])

        barriers = []
        for values in data["well_integrity"]["barriers"].values():
            barriers.append(values)

        retrievables = []
        for values in data["well_integrity"]["retrievable"].values():
            retrievables.append(values)

        questions = []
        for values in data["well_integrity"]["questions"].values():
            questions.append(values)

        wi_impacts = []
        for values in data["well_integrity"]["impact"].values():
            wi_impacts.append(values)

    except Exception as e:
        msg = f"Failed to read JSON from '{filename or 'file'}': {e}"
        print(msg)
        # return msg, no_update
        return msg, no_update, no_update, no_update, no_update, no_update, no_update

    msg = f"Loaded {filename} successfully."
    return msg, answers, wd_impacts, barriers, retrievables, questions, wi_impacts








if __name__ == "__main__":
    app.run(debug=True)