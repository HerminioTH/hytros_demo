from dash import dcc, html, callback, Output, Input, MATCH


cw_1 = 1
cw_2 = 10
cw_3 = 3
cw_4 = 3
cw_5 = 1
cw_6 = 30
cw_7 = 1
cw_8 = 1
cw_9 = 1
cw_10 = 1
cw_11 = 1
cw_12 = 1

def set_style(width, textAlign="left", bold=None, border=False):
    if border:
        border_style = "1px solid #999"
    else:
        border_style = "0px solid #999"
    style = {
        "textAlign": textAlign,
        "verticalAlign": "middle",
        "border": border_style,
        "padding": "10px 0px",        # ← controls space inside cells
        "fontWeight": bold,
        # "width": str(width)+"px",
        "width": str(width)+"%",
        "borderRadius": "5px",
        "backgroundColor": "white"
    }
    return style

def create_barrier_dropdown():
    return dcc.Dropdown(
                            options=[
                                {"label": "Primary", "value": "primary"},
                                {"label": "Secondary", "value": "secondary"}
                            ],
                            value="",      # default selection
                            clearable=False,
                            style={"width": "130px", "textAlign": "center"},
                            searchable=False
                        )

def create_retrievable_dropdown(id_name):
    return dcc.Dropdown(
                            options=[
                                {"label": "Yes", "value": "yes"},
                                {"label": "No", "value": "no"}
                            ],
                            id=id_name,
                            value="",      # default selection
                            clearable=False,
                            style={"width": "80px"},
                            searchable=False
                        )

def create_answer_dropdown(id_name):
    return dcc.Dropdown(
                            options=[
                                {"label": "Yes", "value": "yes"},
                                {"label": "No", "value": "no"},
                                {"label": "Unknown", "value": "unknown"},
                            ],
                            id=id_name,
                            value="",      # default selection
                            clearable=False,
                            style={"width": "100px", "verticalAlign": "middle"},
                            searchable=False
                        )

def create_impact_dropdown(id_name):
    dp_down = dcc.Dropdown(
                            options=[
                                {"label": "Low", "value": "low"},
                                {"label": "Medium", "value": "medium"},
                                {"label": "High", "value": "high"},
                            ],
                            value=None,      # default selection
                            clearable=False,
                            style={
                                "width": "110px",
                                "backgroundColor": "#ffffff"
                            },
                            searchable=False,
                            id=id_name
                        )
    return dp_down

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





tab_well_integrity = dcc.Tab(
    label = "Well Integrity",
    value = "well-integrity",
    children = [
        html.Div(
            style={"maxWidth": "2000px", "margin": "1px auto", "fontFamily": "system-ui"},
            children=[
                html.Table(
                    children=[
                        html.Thead(
                            html.Tr([
                                html.Th("#", style=set_style(cw_1, textAlign="center")),
                                html.Th("Element", style=set_style(cw_2, textAlign="left")),
                                html.Th("Barrier", style=set_style(cw_3, textAlign="left")),
                                html.Th("Retrievable", style=set_style(cw_4)),
                                # html.Th("#", style=set_style(cw_5, textAlign="center")),
                                html.Th("Criteria", style=set_style(cw_6)),
                                # html.Th("Answer", style=set_style(cw_7)),
                                html.Th("Qualified/FFS", style=set_style(cw_8)),
                                html.Th("Material compatibility", style=set_style(cw_9, textAlign="center")),
                                html.Th("Mitigation", style=set_style(cw_10)),
                                html.Th("Impact", style=set_style(cw_11, textAlign="center")),
                                html.Th("", style=set_style(cw_12)),
                            ])
                        ),
                        html.Tbody([

                            ################# Element 1 #################
                            html.Tr([
                                html.Td("1)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Primary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-1"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are there impermeable formations that can constitute a (primary) caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-1-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the fracture gradient higher than the maximum anticipated operating pressure?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-1-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-1", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-1", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-1", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 1}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 1}), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 2 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("2)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-2"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-2-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the production casing / liner it contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-2-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-2-3"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-2", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-2", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-2", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 2}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 2}), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 3 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("3)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Cement behind the production casing / Liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-3"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the production casing/liner(lap) cemented across the caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-3-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is there sufficient cement length of good quality to provide zonal isolation?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-3-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the cement type compatible with expected operating conditions? E.g., Portland API class G cement.", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-3-3"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-3", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-3", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-3", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 3}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 3}), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 4 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("Is there an overlapping casing string behind the production casing / liner across the caprock? If no skip to 6", 
                                    style=set_style(cw_1, textAlign="left", bold="bold"),
                                    colSpan=4
                                    ),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("4)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Overlapping casing behing the production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-4"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-4-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-4-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-4-3"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-4", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-4", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-4", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 4}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 4}), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 5 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("5)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Overlapping casing behing the production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-5"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-5-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-5-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-5-3"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-5", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-5", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-5", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 5}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 5}), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 6 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("6)", style=set_style(cw_1, textAlign="center")),
                                html.Td("Secondary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown("retrievable-6"), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are there impermeable formations that can constitute an additional (secondary) caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-6-1"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the fracture gradient higher than the maximum anticipated operating pressure? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown("q-6-2"), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-6", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-6", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id="mit-6", style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown({"type": "integrity-impact", "i": 6}), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square({"type": "integrity-impact-color", "i": 6}), style=set_style(cw_11, textAlign="center")),
                            ]),
                        ])
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
    Output(component_id={"type": "integrity-impact-color", "i": MATCH}, component_property="style"),
    Input(component_id={"type": "integrity-impact", "i": MATCH}, component_property="value"),
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
        "backgroundColor": mapping.get(value, "#f5f5f5"),
        "margin": "auto",
        "transition": "background-color 0.2s ease",
    }
    print(value, mapping.get(value, "#f5f5f5"))
    return style



################# Element 1 #################
@callback(
    Output(component_id="a-ffs-1", component_property="children"),
    Output(component_id="a-ffs-1", component_property="style"),
    Input(component_id="q-1-2", component_property="value")
)
def qualified_FFS_1(input):
    mapping = {
        "yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "no": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"], style


@callback(
    Output(component_id="a-compat-1", component_property="children"),
    Output(component_id="a-compat-1", component_property="style"),
    Input(component_id="q-1-1", component_property="value")
)
def material_compatibility_1(input):
    mapping = {
        "yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "no": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"], style


@callback(
    Output(component_id="mit-1", component_property="children"),
    Output(component_id="mit-1", component_property="style"),
    Input(component_id="a-ffs-1", component_property="children"),
    Input(component_id="a-compat-1", component_property="children"),
    Input(component_id="retrievable-1", component_property="value")
)
def mitigation_1(H, I, is_retrievable):
    if H == "Unknown" or I == "Unknown":
        text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    elif H == "Yes" and I == "Yes":
        text, bg_color, txt_color = "No or minor", "#a2c543", "#000000"
    elif H == "No" or I == "No":
        if is_retrievable == "no":
            text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
        elif is_retrievable == "yes":
            text, bg_color, txt_color = "Minor", "#43c543", "#000000"
        else:
            text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    else:
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color
    }
    return text, style



################# Element 2 #################
@callback(
    Output(component_id="a-ffs-2", component_property="children"),
    Output(component_id="a-ffs-2", component_property="style"),
    Input(component_id="q-2-2", component_property="value")
)
def qualified_FFS_2(input):
    mapping = {
        "yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "no": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"], style


@callback(
    Output(component_id="a-compat-2", component_property="children"),
    Output(component_id="a-compat-2", component_property="style"),
    Input(component_id="q-2-1", component_property="value")
)
def material_compatibility_2(input):
    mapping = {
        "yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "no": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"], style


@callback(
    Output(component_id="mit-2", component_property="children"),
    Output(component_id="mit-2", component_property="style"),
    Input(component_id="a-ffs-2", component_property="children"),
    Input(component_id="a-compat-2", component_property="children"),
    Input(component_id="retrievable-2", component_property="value")
)
def mitigation_2(H, I, is_retrievable):
    if H == "Unknown" or I == "Unknown":
        text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    elif H == "Yes" and I == "Yes":
        text, bg_color, txt_color = "No or minor", "#a2c543", "#000000"
    elif H == "No" or I == "No":
        if is_retrievable == "no":
            text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
        elif is_retrievable == "yes":
            text, bg_color, txt_color = "Minor", "#43c543", "#000000"
        else:
            text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    else:
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color
    }
    return text, style

