from dash import dcc, html, callback, Output, Input, MATCH
from utils import bid, rid, qid, gid

cw_1 = 2
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

def create_barrier_dropdown(id_name):
    return dcc.Dropdown(
                            options=[
                                {"label": "Primary", "value": "Primary"},
                                {"label": "Secondary", "value": "Secondary"}
                            ],
                            id=id_name,
                            value="",      # default selection
                            clearable=False,
                            style={"width": "130px", "textAlign": "center"},
                            searchable=False
                        )

def create_retrievable_dropdown(id_name):
    return dcc.Dropdown(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"}
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
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                                {"label": "Unknown", "value": "Unknown"},
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
                                {"label": "Low", "value": "Low"},
                                {"label": "Medium", "value": "Medium"},
                                {"label": "High", "value": "High"},
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


def calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    if q1 == "Yes" and q2 == "Yes" and q3 == "Yes":
        text, bg_color, txt_color = "No or minor", "#43c543", "#000000"
    elif q_ffs == "" or q_mat == "":
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    elif q1 == "Unknown" and q2 == "Unknown" and q3 == "Unknown":
        text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    else:
        if is_retrievable == "Yes":
            if q3 == "Yes":
                if q1 == "Yes" or q2 == "Yes":
                    if q1 == "Unknown" or q2 == "Unknown":
                        text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
                    else:
                        text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                elif q1 == "No" or q2 == "No":
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                elif q1 == "Unknown" or q2 == "Unknown":
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
                else:
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
            elif q3 == "Unknown":
                if q1 == "No" or q2 == "No":
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                # elif q1 == "Unknown" or q2 == "Unknown":
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"

            elif q1 == "Yes" and q2 == "Yes":
                if q3 == "No":
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
            else:
                text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
        else:
            if q_mat == "No":
                text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
            else:
                if q1 == "No" or q2 == "No":
                    text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color,
        "transition": "background-color 0.2s ease",
    }
    return text, style


def calculate_mitigation_4q(q1, q2, q3, q4, q_ffs, q_mat, is_retrievable):
    if q1 == "Yes" and q2 == "Yes" and q3 == "Yes" and q4 == "Yes":
        text, bg_color, txt_color = "No or minor", "#43c543", "#000000"
    elif q_ffs == "" or q_mat == "":
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    elif q1 == "Unknown" and q2 == "Unknown" and q3 == "Unknown" and q4 == "Unknown":
        text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    else:
        if is_retrievable == "Yes":
            if q4 == "Yes":
                if q1 == "No" or q2 == "No" or q3 == "No":
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                elif q1 == "Unknown" or q2 == "Unknown" or q3 == "Unknown":
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
            elif q4 == "No":
                text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
            else:
                if q1 == "Yes" and q2 == "Yes" and q3 == "Yes":
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
                elif q1 == "No" or q2 == "No" or q3 == "No":
                    text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
        elif is_retrievable == "No":
            if q_mat == "Yes":
                if q1 == "No" or q2 == "No" or q3 == "No":
                    text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
            elif q_mat == "No":
                text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
            else:
                if q1 == "No" or q2 == "No" or q3 == "No":
                    text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
                else:
                    text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
        else:
            text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color,
        "transition": "background-color 0.2s ease",
    }
    return text, style

def calculate_FFS_2q(q1, q2):
    if q1 == "Unknown" and q2 == "Unknown":
        text = "Unknown"
    elif q1 == "Yes" and q2 == "Yes":
        text = "Yes"
    elif q1 == "Yes" or q2 == "Yes":
        if q1 == "Unknown" or q2 == "Unknown":
            text = "Unknown"
        else:
            text = "No"
    elif q1 == "No" or q2 == "No":
        text = "No"
    else:
        text = ""
    return text

def calculate_FFS_3q(q1, q2, q3):
    if q1 == "No" or q2 == "No" or q3 == "No":
        text = "No"
    elif q1 == "Unknown" or q2 == "Unknown" or q3 == "Unknown":
        text = "Unknown"
    elif q1 == "Yes" and q2 == "Yes" and q3 == "Yes":
        text = "Yes"
    else:
        text = ""
    return text




tab_well_integrity = dcc.Tab(
    label = "Well Integrity",
    value = "well-integrity",
    children = [
        html.Div(
            style={"maxWidth": "2000px", "margin": "16px auto", "fontFamily": "system-ui"},
            children=[
                html.Table(
                    children=[
                        html.Thead(
                            html.Tr([
                                html.Th("#", style=set_style(cw_1, textAlign="left")),
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
                                html.Td("1)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Primary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-1")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-1")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are there impermeable formations that can constitute a (primary) caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-1-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the fracture gradient higher than the maximum anticipated operating pressure?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-1-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-1", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-1", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 1), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 1)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 1)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 2 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("2)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-2")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-2")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-2-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the production casing/liner contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-2-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-2-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-2", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-2", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 2), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 2)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 2)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 3 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("3)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Cement behind the production casing / Liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-3")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-3")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the production casing/liner(lap) cemented across the caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-3-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is there sufficient cement length of good quality to provide zonal isolation?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-3-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the cement type compatible with expected operating conditions? E.g., Portland API class G cement.", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-3-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-3", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-3", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 3), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 3)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 3)), style=set_style(cw_11, textAlign="center")),
                            ]),
                            
                            ################# Skip to 6 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("Is there an overlapping casing string behind the production casing/liner across the caprock? If no, skip to 6.", 
                                    style=set_style(cw_1, textAlign="left", bold="bold"),
                                    colSpan=4
                                    ),
                            html.Td("", style=set_style(cw_1, textAlign="center")),

                            ################# Element 4 #################
                            html.Tr([
                                html.Td("4)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Overlapping casing behing the production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-4")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-4")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-4-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-4-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-4-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-4", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-4", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 4), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 4)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 4)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 5 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("5)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Cement behind the overlapping casing", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-5")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-5")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-5-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-5-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-5-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-5", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-5", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 5), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 5)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 5)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 6 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("6)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Secondary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-6")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-6")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are there impermeable formations that can constitute an additional (secondary) caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-6-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the fracture gradient higher than the maximum anticipated operating pressure? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-6-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-6", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-6", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 6), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 6)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 6)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 7 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("7)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Casing string across the secondary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-7")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-7")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-7-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-7-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-7-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-7", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-7", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 7), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 7)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 7)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 8 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("8)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Cement behind the casing string across the secondary caprock", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-8")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-8")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing cemented across the secondary caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-8-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is there sufficient cement length of good quality to provide zonal isolation?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-8-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the cement type compatible with expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-8-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-8", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-8", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 8), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 8)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 8)), style=set_style(cw_11, textAlign="center")),
                            ]),
                            
                            ################# Skip to 11 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("Is there an overlapping casing string across the caprock? If no, skip to 11.", 
                                    style=set_style(cw_1, textAlign="left", bold="bold"),
                                    colSpan=4
                                    ),
                            html.Td("", style=set_style(cw_1, textAlign="center")),

                            ################# Element 9 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("9)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Overlapping casing behind the production casing / liner", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-9")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-9")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the casing inspected and free of any defects (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-9-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Does the casing contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-9-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the casing material compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-9-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-9", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-9", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 9), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 9)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 9)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 10 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("10)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Cement behind the overlapping casing", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-10")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-10")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the overlapping casing cemented across the caprock?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-10-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is there sufficient cement length of good quality to provide zonal isolation? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-10-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Is the cement type compatible with expected operating conditions? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-10-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-10", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-10", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 10), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 10)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 10)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 11 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("11)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Wellhead", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-11")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-11")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are all wellhead components inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-11-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Have all wellhead components been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-11-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are all  materials compatible and designed for hydrogen environment? E.g. metal-to-metal seals, less connections", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-11-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-11", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-11", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 11), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 11)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 11)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 12 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("12)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Other non-retrievable completion e.g. sand screens", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-12")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-12")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are all components inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-12-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Have all components been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-12-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are the materials compatible with expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-12-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-12", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-12", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 12), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 12)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 12)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 13 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("13)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Production packer", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-13")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-13")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Has packer functionality been verified through testing as per applicable guideliness, standards or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-13-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the packer positioned across the caprock with a good quality cement behind cement string(s)?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-13-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are all packer materials (e.g. elastomer and steel) compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-13-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-13", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-13", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 13), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 13)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 13)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 14 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("14)", style=set_style(cw_1, textAlign="left")),
                                html.Td("SSSV", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-14")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-14")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the SSSV surface controlled? ", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-14-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Is the SSV inspected and free of any defect as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-14-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Has the SSSV been verified through functional testing (e.g. pressure and leakage testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-14-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("4. Are all SSSV component materials compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-14-4")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-14", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-14", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 14), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 14)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 14)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 15 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("15)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Tubing", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-15")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-15")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Is the tubing string inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-15-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Has the tubing string been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-15-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Does the tubing string contain gas-tight (premium) connections?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-15-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("4. Is the tubing string material compatible with the expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-15-4")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-15", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-15", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 15), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 15)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 15)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 16 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("16)", style=set_style(cw_1, textAlign="left")),
                                html.Td("X-mas tree and valves", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-16")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-16")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are all x-mas tree components inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-16-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Have all x-mas tree components been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-16-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are all x-mas tree materials compatible and designed for hydrogen environment? E.g. metal-to-metal seals, less connections", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-16-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-16", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-16", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 16), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 16)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 16)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 17 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("17)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Wellhead casing spools and hangers", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-17")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-17")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are all wellhead components inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-17-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Have all wellhead components been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-17-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are all wellhead materials compatible and designed for hydrogen environment? E.g. metal-to-metal seals, less connections", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-17-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-17", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-17", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 17), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 17)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 17)), style=set_style(cw_11, textAlign="center")),
                            ]),

                            ################# Element 18 #################
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            html.Td("", style=set_style(cw_1, textAlign="center")),
                            
                            html.Tr([
                                html.Td("18)", style=set_style(cw_1, textAlign="left")),
                                html.Td("Any other completion e.g.. Sliding side doors, side pocket mandrels, landing nipples etc", style=set_style(cw_2, textAlign="left")),
                                html.Td(create_barrier_dropdown(bid("well_integrity", "barrier-18")), style=set_style(cw_3, textAlign="center")),
                                html.Td(create_retrievable_dropdown(rid("well_integrity", "retrievable-18")), style=set_style(cw_4)),
                                html.Tr([
                                        html.Td("1. Are all components inspected and free of any defect (e.g. corrosion) as per applicable requirements?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-18-1")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("2. Have all components been verified through functional testing (e.g. pressure testing) as required by applicable standards, guidelines, or regulations?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-18-2")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Tr([
                                        html.Td("3. Are the materials compatible with expected operating conditions?", style=set_style(cw_6)),
                                        html.Td(create_answer_dropdown(qid("well_integrity", "q-18-3")), style=set_style(cw_8, textAlign="right"))
                                    ]
                                ),
                                html.Td("", id="a-ffs-18", style=set_style(cw_7, textAlign="center")),
                                html.Td("", id="a-compat-18", style=set_style(cw_8, textAlign="center")),
                                html.Td("", id=gid("well_integrity", "mitigation", 18), style=set_style(cw_9, textAlign="center")),
                                html.Td(create_impact_dropdown(gid("well_integrity", "impact", 18)), style=set_style(cw_10, textAlign="center")),
                                html.Td(create_color_square(gid("well_integrity", "impact-color", 18)), style=set_style(cw_11, textAlign="center")),
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
    Output(component_id=gid("well_integrity", "impact-color", MATCH), component_property="style"),
    Input(component_id=gid("well_integrity", "impact", MATCH), component_property="value"),
)
def change_impact_color(value):
    mapping = {
        "Low": "#43c5437f",
        "Medium": "#fff13081",
        "High": "#c027277b"
    }
    style={
        "width": "24px",
        "height": "24px",
        "borderRadius": "5px",
        "backgroundColor": mapping.get(value, "#f5f5f5"),
        "margin": "auto",
        "transition": "background-color 0.2s ease",
    }
    return style



################# Element 1 #################
@callback(
    Output(component_id="a-ffs-1", component_property="children"),
    # Output(component_id="a-ffs-1", component_property="style"),
    Input(component_id=qid("well_integrity", "q-1-2"), component_property="value")
)
def qualified_FFS_1(input):
    mapping = {
        "Yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "No": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "Unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["Unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"]#, style


@callback(
    Output(component_id="a-compat-1", component_property="children"),
    # Output(component_id="a-compat-1", component_property="style"),
    Input(component_id=qid("well_integrity", "q-1-1"), component_property="value")
)
def material_compatibility_1(input):
    mapping = {
        "Yes": {"bg_color": "#43c54381", "tx_color": "#000000", "text": "Yes"},
        "No": {"bg_color": "#c0272783", "tx_color": "#FFFFFF", "text": "No"},
        "Unknown": {"bg_color": "#4E4E4E", "tx_color": "#FFFFFF", "text": "Unknown"},
        "": {"bg_color": "#f5f5f5", "tx_color": "#FFFFFF", "text": ""},
    }
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "backgroundColor": "#4E4E4E"
    }
    selected = mapping.get(input, mapping["Unknown"])
    style["backgroundColor"] = selected["bg_color"]
    style["color"] = selected["tx_color"]
    style["fontWeight"] = "bold"
    style["transition"] = "background-color 200ms ease"
    return selected["text"]#, style


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 1), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 1), component_property="style"),
    Input(component_id="a-ffs-1", component_property="children"),
    Input(component_id="a-compat-1", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-1"), component_property="value")
)
def mitigation_1(q_ffs, q_mat, is_retrievable):
    if q_ffs == "Yes" and q_mat == "Yes":
        text, bg_color, txt_color = "No or minor", "#43c543", "#000000"
    elif q_ffs == "" or q_mat == "":
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    else:
        if is_retrievable == "Yes":
            if q_ffs == "No" or q_mat == "No":
                text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
            else:
                text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
        else: # if is_retrievable == "No":
            if q_ffs == "No" or q_mat == "No":
                text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
            else:
                text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color,
        "transition": "background-color 0.2s ease",
    }
    return text, style



################# Element 2 #################
@callback(
    Output(component_id="a-ffs-2", component_property="children"),
    Input(component_id=qid("well_integrity", "q-2-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-2-2"), component_property="value"),
)
def qualified_FFS_2(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-2", component_property="children"),
    Input(component_id=qid("well_integrity", "q-2-3"), component_property="value"),
)
def material_compatibility_2(q3):
    return q3


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 2), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 2), component_property="style"),
    Input(component_id=qid("well_integrity", "q-2-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-2-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-2-3"), component_property="value"),
    Input(component_id="a-ffs-2", component_property="children"),
    Input(component_id="a-compat-2", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-2"), component_property="value")
)
def mitigation_2(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 3 #################
@callback(
    Output(component_id="a-ffs-3", component_property="children"),
    Input(component_id=qid("well_integrity", "q-3-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-3-2"), component_property="value")
)
def qualified_FFS_3(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-3", component_property="children"),
    Input(component_id=qid("well_integrity", "q-3-3"), component_property="value"),
)
def material_compatibility_3(q33):
    return q33


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 3), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 3), component_property="style"),
    Input(component_id=qid("well_integrity", "q-3-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-3-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-3-3"), component_property="value"),
    Input(component_id="a-ffs-3", component_property="children"),
    Input(component_id="a-compat-3", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-3"), component_property="value")
)
def mitigation_3(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 4 #################
@callback(
    Output(component_id="a-ffs-4", component_property="children"),
    Input(component_id=qid("well_integrity", "q-4-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-4-2"), component_property="value")
)
def qualified_FFS_4(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-4", component_property="children"),
    Input(component_id=qid("well_integrity", "q-4-3"), component_property="value")
)
def material_compatibility_4(q43):
    return q43


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 4), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 4), component_property="style"),
    Input(component_id=qid("well_integrity", "q-4-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-4-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-4-3"), component_property="value"),
    Input(component_id="a-ffs-4", component_property="children"),
    Input(component_id="a-compat-4", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-4"), component_property="value")
)
def mitigation_4(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 5 #################
@callback(
    Output(component_id="a-ffs-5", component_property="children"),
    Input(component_id=qid("well_integrity", "q-5-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-5-2"), component_property="value")
)
def qualified_FFS_5(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-5", component_property="children"),
    Input(component_id=qid("well_integrity", "q-5-3"), component_property="value")
)
def material_compatibility_5(q53):
    return q53


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 5), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 5), component_property="style"),
    Input(component_id=qid("well_integrity", "q-5-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-5-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-5-3"), component_property="value"),
    Input(component_id="a-ffs-5", component_property="children"),
    Input(component_id="a-compat-5", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-5"), component_property="value")
)
def mitigation_5(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 6 #################
@callback(
    Output(component_id="a-ffs-6", component_property="children"),
    Input(component_id=qid("well_integrity", "q-6-1"), component_property="value")
)
def qualified_FFS_6(q61):
    return q61


@callback(
    Output(component_id="a-compat-6", component_property="children"),
    Input(component_id=qid("well_integrity", "q-6-2"), component_property="value")
)
def material_compatibility_6(q62):
    return q62


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 6), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 6), component_property="style"),
    Input(component_id="a-ffs-6", component_property="children"),
    Input(component_id="a-compat-6", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-6"), component_property="value")
)
def mitigation_6(q_ffs, q_mat, is_retrievable):
    if q_ffs == "Yes" and q_mat == "Yes":
        text, bg_color, txt_color = "No or minor", "#43c543", "#000000"
    elif q_ffs == "" or q_mat == "":
        text, bg_color, txt_color = "", "#f5f5f5", "#FFFFFF"
    else:
        if is_retrievable == "Yes":
            if q_ffs == "No" or q_mat == "No":
                text, bg_color, txt_color = "Moderate", "#fff130", "#000000"
            else:
                text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
        else: # if is_retrievable == "No":
            if q_ffs == "No" or q_mat == "No":
                text, bg_color, txt_color = "Severe", "#c02727", "#FFFFFF"
            else:
                text, bg_color, txt_color = "Unknown", "#4E4E4E", "#FFFFFF"
    style = {
        "textAlign": "center",
        "verticalAlign": "middle",
        "borderRadius": "5px",
        "fontWeight": "bold",
        "color": txt_color,
        "backgroundColor": bg_color
    }
    return text, style



################# Element 7 #################
@callback(
    Output(component_id="a-ffs-7", component_property="children"),
    Input(component_id=qid("well_integrity", "q-7-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-7-2"), component_property="value")
)
def qualified_FFS_7(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-7", component_property="children"),
    Input(component_id=qid("well_integrity", "q-7-3"), component_property="value"),
)
def material_compatibility_7(q73):
    return q73


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 7), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 7), component_property="style"),
    Input(component_id=qid("well_integrity", "q-7-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-7-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-7-3"), component_property="value"),
    Input(component_id="a-ffs-7", component_property="children"),
    Input(component_id="a-compat-7", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-7"), component_property="value")
)
def mitigation_7(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 8 #################
@callback(
    Output(component_id="a-ffs-8", component_property="children"),
    Input(component_id=qid("well_integrity", "q-8-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-8-2"), component_property="value")
)
def qualified_FFS_8(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-8", component_property="children"),
    Input(component_id=qid("well_integrity", "q-8-3"), component_property="value"),
)
def material_compatibility_8(q83):
    return q83


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 8), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 8), component_property="style"),
    Input(component_id=qid("well_integrity", "q-8-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-8-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-8-3"), component_property="value"),
    Input(component_id="a-ffs-8", component_property="children"),
    Input(component_id="a-compat-8", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-8"), component_property="value")
)
def mitigation_8(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 9 #################
@callback(
    Output(component_id="a-ffs-9", component_property="children"),
    Input(component_id=qid("well_integrity", "q-9-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-9-2"), component_property="value")
)
def qualified_FFS_9(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-9", component_property="children"),
    Input(component_id=qid("well_integrity", "q-9-3"), component_property="value")
)
def material_compatibility_9(q93):
    return q93


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 9), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 9), component_property="style"),
    Input(component_id=qid("well_integrity", "q-9-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-9-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-9-3"), component_property="value"),
    Input(component_id="a-ffs-9", component_property="children"),
    Input(component_id="a-compat-9", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-9"), component_property="value")
)
def mitigation_9(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 10 #################
@callback(
    Output(component_id="a-ffs-10", component_property="children"),
    Input(component_id=qid("well_integrity", "q-10-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-10-2"), component_property="value")
)
def qualified_FFS_10(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-10", component_property="children"),
    Input(component_id=qid("well_integrity", "q-10-3"), component_property="value"),
)
def material_compatibility_10(q103):
    return q103


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 10), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 10), component_property="style"),
    Input(component_id=qid("well_integrity", "q-10-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-10-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-10-3"), component_property="value"),
    Input(component_id="a-ffs-10", component_property="children"),
    Input(component_id="a-compat-10", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-10"), component_property="value")
)
def mitigation_10(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 11 #################
@callback(
    Output(component_id="a-ffs-11", component_property="children"),
    # Output(component_id="a-ffs-11", component_property="style"),
    Input(component_id=qid("well_integrity", "q-11-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-11-2"), component_property="value"),
)
def qualified_FFS_11(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-11", component_property="children"),
    Input(component_id=qid("well_integrity", "q-11-3"), component_property="value"),
)
def material_compatibility_11(q113):
    return q113


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 11), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 11), component_property="style"),
    Input(component_id=qid("well_integrity", "q-11-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-11-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-11-3"), component_property="value"),
    Input(component_id="a-ffs-11", component_property="children"),
    Input(component_id="a-compat-11", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-11"), component_property="value")
)
def mitigation_11(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 12 #################
@callback(
    Output(component_id="a-ffs-12", component_property="children"),
    Input(component_id=qid("well_integrity", "q-12-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-12-2"), component_property="value"),
)
def qualified_FFS_12(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-12", component_property="children"),
    Input(component_id=qid("well_integrity", "q-12-3"), component_property="value"),
)
def material_compatibility_12(q123):
    return q123


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 12), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 12), component_property="style"),
    Input(component_id=qid("well_integrity", "q-12-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-12-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-12-3"), component_property="value"),
    Input(component_id="a-ffs-12", component_property="children"),
    Input(component_id="a-compat-12", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-12"), component_property="value")
)
def mitigation_12(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 13 #################
@callback(
    Output(component_id="a-ffs-13", component_property="children"),
    Input(component_id=qid("well_integrity", "q-13-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-13-2"), component_property="value"),
)
def qualified_FFS_13(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-13", component_property="children"),
    Input(component_id=qid("well_integrity", "q-13-3"), component_property="value"),
)
def material_compatibility_13(q133):
    return q133


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 13), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 13), component_property="style"),
    Input(component_id=qid("well_integrity", "q-13-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-13-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-13-3"), component_property="value"),
    Input(component_id="a-ffs-13", component_property="children"),
    Input(component_id="a-compat-13", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-13"), component_property="value")
)
def mitigation_13(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 14 #################
@callback(
    Output(component_id="a-ffs-14", component_property="children"),
    # Output(component_id="a-ffs-14", component_property="style"),
    Input(component_id=qid("well_integrity", "q-14-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-14-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-14-3"), component_property="value"),
)
def qualified_FFS_14(q141, q142, q143):
    if q141 == "Unknown" or q142 == "Unknown" or q143 == "Unknown":
        text = "Unknown"
    elif q141 == "Yes" and q142 == "Yes" and q143 == "Yes":
        text = "Yes"
    elif q141 == "No" or q142 == "No" or q143 == "No":
        text = "No"
    else:
        text = ""
    return text


@callback(
    Output(component_id="a-compat-14", component_property="children"),
    Input(component_id=qid("well_integrity", "q-14-4"), component_property="value"),
)
def material_compatibility_14(q144):
    return q144


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 14), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 14), component_property="style"),
    Input(component_id=qid("well_integrity", "q-14-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-14-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-14-3"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-14-4"), component_property="value"),
    Input(component_id="a-ffs-14", component_property="children"),
    Input(component_id="a-compat-14", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-14"), component_property="value")
)
def mitigation_14(q1, q2, q3, q4, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_4q(q1, q2, q3, q4, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 15 #################
@callback(
    Output(component_id="a-ffs-15", component_property="children"),
    # Output(component_id="a-ffs-15", component_property="style"),
    Input(component_id=qid("well_integrity", "q-15-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-15-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-15-3"), component_property="value"),
)
def qualified_FFS_15(q1, q2, q3):
    text = calculate_FFS_3q(q1, q2, q3)
    return text


@callback(
    Output(component_id="a-compat-15", component_property="children"),
    Input(component_id=qid("well_integrity", "q-15-4"), component_property="value"),
)
def material_compatibility_15(q154):
    return q154


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 15), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 15), component_property="style"),
    Input(component_id=qid("well_integrity", "q-15-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-15-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-15-3"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-15-4"), component_property="value"),
    Input(component_id="a-ffs-15", component_property="children"),
    Input(component_id="a-compat-15", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-15"), component_property="value")
)
def mitigation_15(q1, q2, q3, q4, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_4q(q1, q2, q3, q4, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 16 #################
@callback(
    Output(component_id="a-ffs-16", component_property="children"),
    # Output(component_id="a-ffs-16", component_property="style"),
    Input(component_id=qid("well_integrity", "q-16-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-16-2"), component_property="value"),
)
def qualified_FFS_16(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-16", component_property="children"),
    Input(component_id=qid("well_integrity", "q-16-3"), component_property="value"),
)
def material_compatibility_16(q163):
    return q163


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 16), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 16), component_property="style"),
    Input(component_id=qid("well_integrity", "q-16-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-16-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-16-3"), component_property="value"),
    Input(component_id="a-ffs-16", component_property="children"),
    Input(component_id="a-compat-16", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-16"), component_property="value")
)
def mitigation_16(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 17 #################
@callback(
    Output(component_id="a-ffs-17", component_property="children"),
    Input(component_id=qid("well_integrity", "q-17-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-17-2"), component_property="value"),
)
def qualified_FFS_17(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-17", component_property="children"),
    Input(component_id=qid("well_integrity", "q-17-3"), component_property="value"),
)
def material_compatibility_17(q173):
    return q173


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 17), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 17), component_property="style"),
    Input(component_id=qid("well_integrity", "q-17-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-17-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-17-3"), component_property="value"),
    Input(component_id="a-ffs-17", component_property="children"),
    Input(component_id="a-compat-17", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-17"), component_property="value")
)
def mitigation_17(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style



################# Element 18 #################
@callback(
    Output(component_id="a-ffs-18", component_property="children"),
    # Output(component_id="a-ffs-18", component_property="style"),
    Input(component_id=qid("well_integrity", "q-18-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-18-2"), component_property="value"),
)
def qualified_FFS_18(q1, q2):
    text = calculate_FFS_2q(q1, q2)
    return text


@callback(
    Output(component_id="a-compat-18", component_property="children"),
    Input(component_id=qid("well_integrity", "q-18-3"), component_property="value"),
)
def material_compatibility_18(q183):
    return q183


@callback(
    Output(component_id=gid("well_integrity", "mitigation", 18), component_property="children"),
    Output(component_id=gid("well_integrity", "mitigation", 18), component_property="style"),
    Input(component_id=qid("well_integrity", "q-18-1"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-18-2"), component_property="value"),
    Input(component_id=qid("well_integrity", "q-18-3"), component_property="value"),
    Input(component_id="a-ffs-18", component_property="children"),
    Input(component_id="a-compat-18", component_property="children"),
    Input(component_id=rid("well_integrity", "retrievable-18"), component_property="value")
)
def mitigation_18(q1, q2, q3, q_ffs, q_mat, is_retrievable):
    text, style = calculate_mitigation_3q(q1, q2, q3, q_ffs, q_mat, is_retrievable)
    return text, style

