from dash import dcc, html, callback, Output, Input, MATCH


def set_style(width, padding="15px", textAlign="left", border=False):
    if border:
        border_style = "1px solid #999"
    else:
        border_style = "0px solid #999"
    style = {
        "textAlign": textAlign,
        "border": border_style,
        "padding": padding,        # ← controls space inside cells
        "width": str(width)+"px",
        "borderRadius": "5px",
    }
    return style

cw_1 = 1
cw_2 = 100
cw_3 = 800
cw_4 = 100
cw_5 = 100
cw_6 = 1
cw_7 = 1

def create_answer_dropdown(id_name="answer-dropdown"):
    return dcc.Dropdown(
                            options=[
                                {"label": "Yes", "value": "yes"},
                                {"label": "No", "value": "no"},
                                {"label": "Unknown", "value": "unknown"},
                            ],
                            value="",      # default selection
                            clearable=False,
                            style={"width": "120px"},
                            searchable=False,
                            id=id_name
                        )

def create_impact_dropdown(id_name="impact-dropdown"):
    dp_down = dcc.Dropdown(
                            options=[
                                {"label": "Low", "value": "low"},
                                {"label": "Medium", "value": "medium"},
                                {"label": "High", "value": "high"},
                            ],
                            value=None,      # default selection
                            clearable=False,
                            style={
                                "width": "120px",
                                "backgroundColor": "#ffffff"
                            },
                            searchable=False,
                            id=id_name
                        )
    return dp_down
    # return html.Div(dp_down, id=id_name)

def create_color_square(id_name="sq", color="#4E4E4E", size=24):
    square = html.Div(
        style={
            "width": f"{size}px",
            "height": f"{size}px",
            "borderRadius": "5px",
            "backgroundColor": color,
        },
        id=id_name,
    )
    return square

tab_well_design = dcc.Tab(
    label = "Well Design",
    value = "well-design",
    children = [
        html.Div(
            style={"maxWidth": "2000px", "margin": "16px auto", "fontFamily": "system-ui"},
            children=[
                html.Table(
                    [
                        html.Thead(
                            html.Tr([
                                html.Th("#", style=set_style(cw_1)),
                                html.Th("Criteria category", style=set_style(cw_2)),
                                html.Th("Criteria sub-category", style=set_style(cw_3)),
                                html.Th("Answer", style=set_style(cw_4)),
                                html.Th("Mitigation", style=set_style(cw_5)),
                                html.Th("Impact", style=set_style(cw_6)),
                                html.Th("", style=set_style(cw_7)),
                            ])
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td("1", style=set_style(cw_1)),
                                html.Td("Acessibility", style=set_style(cw_2)),
                                html.Td("Is the well accessible?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-1"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="1-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 1}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 1}, size=24)),
                            ],
                            # id = "row-1",
                            # style = {"display": "table-row"}
                            ),
                            html.Tr([
                                html.Td("2", style=set_style(cw_1)),
                                html.Td("Age", style=set_style(cw_2)),
                                html.Td("Is the well constructed before 1996?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-2"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="2-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 2}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 2}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("3", style=set_style(cw_1)),
                                html.Td("Type/function", style=set_style(cw_2)),
                                html.Td("Was the well used as injector e.g. brine for pressure maintenance? ", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-3"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="3-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 3}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 3}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("4", style=set_style(cw_1)),
                                html.Td("Depth", style=set_style(cw_2)),
                                html.Td("Is chage in target depth required? For example, drilling or sidetracking to reach deeper zones, or perforating, milling shallower intervals. ", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-4"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="4-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 4}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 4}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("5", style=set_style(cw_1)),
                                html.Td("Diameter", style=set_style(cw_2)),
                                html.Td("Is the well diameter sufficient for the expected operational conditions and performance?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-5"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="5-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 5}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 5}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("6", style=set_style(cw_1)),
                                html.Td("Deviation", style=set_style(cw_2)),
                                html.Td("Is the inclination of the well across the caprock(s) higher than 30 degrees?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-6"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="6-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 6}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 6}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("7", style=set_style(cw_1)),
                                html.Td("Geological and geomechanical occurances", style=set_style(cw_2)),
                                html.Td("Are there indication of geological or geomehcanical mechanisms (e.g. tectonic forces, presence of fractures and faults etc) that could have an affect on the components of the well that provide structural integrity i.e. wellhead, conductor casing?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-7"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="7-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 7}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 7}, size=24)),
                            ]),
                            html.Tr([
                                html.Td("8", style=set_style(cw_1)),
                                html.Td("Operational issues", style=set_style(cw_2)),
                                html.Td("Has the well experienced any integrity issues, such as sustained casing pressure (SCP) or leakage in any relevant annulus?", style=set_style(cw_3)),
                                html.Td(create_answer_dropdown("question-8"), style=set_style(cw_4)),
                                html.Td("Unknown", style=set_style(cw_5), id="8-mitigation"),
                                html.Td(create_impact_dropdown({"type": "impact", "i": 8}), style=set_style(cw_6)),
                                html.Td(create_color_square({"type": "impact-color", "i": 8}, size=24)),
                            ]),
                        ]),
                    ],
                    style={
                        "width": "90%",
                    }
                )
            ]
        )
    ]
)

@callback(
    Output(component_id="1-mitigation", component_property="style"),
    Output(component_id="1-mitigation",  component_property="children"),
    Input(component_id="question-1",  component_property="value"),
)
def mitigation_1(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#43c543", "tx_color": "#000000", "text": "No or minor"},
        "no": {"bg_color": "#c02727", "tx_color": "#FFFFFF", "text": "Severe"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="2-mitigation", component_property="style"),
    Output(component_id="2-mitigation",  component_property="children"),
    Input(component_id="question-2",  component_property="value"),
)
def mitigation_2(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#fff130", "tx_color": "#000000", "text": "Moderate"},
        "no": {"bg_color": "#ffffff", "tx_color": "#FFFFFF", "text": ""},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="3-mitigation", component_property="style"),
    Output(component_id="3-mitigation",  component_property="children"),
    Input(component_id="question-3",  component_property="value"),
)
def mitigation_3(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#fff130", "tx_color": "#000000", "text": "Moderate"},
        "no": {"bg_color": "#ffffff", "tx_color": "#FFFFFF", "text": ""},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="4-mitigation", component_property="style"),
    Output(component_id="4-mitigation",  component_property="children"),
    Input(component_id="question-4",  component_property="value"),
)
def mitigation_4(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#c02727", "tx_color": "#FFFFFF", "text": "Severe"},
        "no": {"bg_color": "#43c543", "tx_color": "#000000", "text": "No or minor"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="5-mitigation", component_property="style"),
    Output(component_id="5-mitigation",  component_property="children"),
    Input(component_id="question-5",  component_property="value"),
)
def mitigation_5(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#43c543", "tx_color": "#000000", "text": "No or minor"},
        "no": {"bg_color": "#c02727", "tx_color": "#FFFFFF", "text": "Severe"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="6-mitigation", component_property="style"),
    Output(component_id="6-mitigation",  component_property="children"),
    Input(component_id="question-6",  component_property="value"),
)
def mitigation_6(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#fff130", "tx_color": "#000000", "text": "Moderate"},
        "no": {"bg_color": "#ffffff", "tx_color": "#FFFFFF", "text": ""},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="7-mitigation", component_property="style"),
    Output(component_id="7-mitigation",  component_property="children"),
    Input(component_id="question-7",  component_property="value"),
)
def mitigation_7(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#c02727", "tx_color": "#FFFFFF", "text": "Severe"},
        "no": {"bg_color": "#43c543", "tx_color": "#000000", "text": "No or minor"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]

@callback(
    Output(component_id="8-mitigation", component_property="style"),
    Output(component_id="8-mitigation",  component_property="children"),
    Input(component_id="question-8",  component_property="value"),
)
def mitigation_8(status):
    style = set_style(cw_5)
    mapping = {
        "yes": {"bg_color": "#fff130", "tx_color": "#000000", "text": "Moderate"},
        "no": {"bg_color": "#ffffff", "tx_color": "#FFFFFF", "text": ""},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#FFFFFF", "tx_color": "#FFFFFF", "text": ""},
    }
    selected = mapping.get(status, mapping[status])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return style, selected["text"]


@callback(
    Output(component_id={"type": "impact-color", "i": MATCH}, component_property="style"),
    Input(component_id={"type": "impact", "i": MATCH}, component_property="value"),
)
def change_impact_color(value):
    mapping = {
        "low": "#43c5437f",
        "medium": "#fff13081",
        "high": "#c027277b"
    }
    style={
        "width": "24px",
        "height": "24px",
        "borderRadius": "5px",
        "backgroundColor": mapping.get(value, "#FFFFFF"),
        "margin": "auto",
        "transition": "background-color 0.2s ease",
    }
    return style