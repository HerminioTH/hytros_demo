import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input
from utils import fid


style_1 = {
    "textAlign": "right",
    "padding": "10px",
    "width": "20px",
    "fontWeight": "bold"
}

style_2 = {
    "padding": "10px",
    "width": "100px",
    "fontWeight": "normal"
}

def create_dropdown():
    drop = dcc.Dropdown(
                            options=[
                                {"label": "K55 (API 5CT)", "value": "K55 (API 5CT)"},
                                {"label": "J55 (API 5CT)", "value": "J55 (API 5CT)"},
                                {"label": "L80 (API 5CT)", "value": "L80 (API 5CT)"},
                                {"label": "N80 (API 5CT)", "value": "N80 (API 5CT)"},
                                {"label": "P110 (API 5CT)", "value": "P110 (API 5CT)"},
                                {"label": "T95 (API 5CT)", "value": "T95 (API 5CT)"},
                                {"label": "42CrMo4 (QT/QTT)", "value": "42CrMo4 (QT/QTT)"},
                                {"label": "P235", "value": "P235"},
                                {"label": "L360", "value": "L360"},
                                {"label": "AISI 316 (stainless) (Cr 16-18%, Ni 10-14%, Mb 2-3%)", "value": "AISI 316 (stainless) (Cr 16-18%, Ni 10-14%, Mb 2-3%)"},
                                {"label": "IN718 (Ni-base superalloy)", "value": "IN718 (Ni-base superalloy)"},
                                {"label": "34CrMo4", "value": "34CrMo4"},
                                {"label": "HAZ X65", "value": "HAZ X65"},
                                {"label": "BM X65", "value": "BM X65"},
                                {"label": "WM X65", "value": "WM X65"},
                                {"label": "BM X80", "value": "BM X80"},
                                {"label": "VM55W", "value": "VM55W"},
                                {"label": "VM80W", "value": "VM80W"},
                                {"label": "VM80S", "value": "VM80S"},
                                {"label": "VM95SS", "value": "VM95SS"},
                                {"label": "VM110SS", "value": "VM110SS"},
                            ],
                            value="",      # default selection
                            clearable=False,
                            style={"width": "220px"},
                            searchable=False,
                            id=fid("tab_material", "mat-selector")
                        )
    return drop

tab_materials = dcc.Tab(
        label="Material compatibility",
        value="mat-compat",
        children=[
            html.Br(),

            html.Div(
                style={"width": "100%", "margin": "16px auto", "fontFamily": "system-ui"},
                children=[
                    html.Table(
                        [
                            html.Tbody([
                                html.Tr([
                                    html.Td("Steel Type / Grade:", style=style_1),
                                    html.Td(create_dropdown(), id=fid("tab_material", "cell-1"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Result:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-2"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Final state:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-3"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Failure mode / observation:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-4"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Test conditions:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-5"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Time:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-6"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("% H₂:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-7"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Pressure (bar):", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-8"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Temperature (°C):", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-9"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Test type:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-10"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Yield strenght (MPa):", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-11"), style=style_2),
                                ]),
                                html.Tr([
                                    html.Td("Study / Source:", style=style_1),
                                    html.Td("", id=fid("tab_material", "cell-12"), style=style_2),
                                ]),
                            ]),
                        ],
                        id=fid("tab_material", "mat-details"),
                        style={"width": "100%"}
                    )
                ]
            )

            
        ]
    )

@callback(
    Output(component_id=fid("tab_material", "cell-2"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-3"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-4"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-5"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-6"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-7"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-8"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-9"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-10"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-11"), component_property="children"),
    Output(component_id=fid("tab_material", "cell-12"), component_property="children"),
    Input(component_id=fid("tab_material", "mat-selector"), component_property="value"),
    prevent_initial_call=True,
)
def show_details(material):
    print(material)

    mapping = {
        "": {
            "result": "-",
            "condition": "-",
            "final_state": "-",
            "failure_mode": "-",
            "test_conditions": "-",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "-",
            "pressure": "-",
            "temperature": "-",
            "test_type": "-",
            "yield": "-",
            "source": "_"
        },
        "K55 (API 5CT)": {
            "result": "Validated",
            "condition": "Field & Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "No structural damage; good integrity",
            "failure_mode": "Corrosion at surface, no strength loss",
            "test_conditions": "Exposed to H₂; casing/tubing",
            "time": "1000 h",
            "other_contaminants": "Sour gas / brine",
            "h2_percentage": "100% / 10%",
            "pressure": "100",
            "temperature": "100",
            "test_type": "Field & Lab",
            "yield": "517",
            "source": "HyStories (Loder, 2023); RAG (2017); Boersheim et al. (2019)"
        },
        "J55 (API 5CT)": {
            "result": "Validated but slight effect on steel",
            "condition": "Field & Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Slight ductility reduction; integrity maintained",
            "failure_mode": "None significant; no HIC or HE",
            "test_conditions": "Electrochemical & gas exposure",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "100%",
            "pressure": "100",
            "temperature": "100",
            "test_type": "Laboratory",
            "yield": "517",
            "source": "Iorio et al. (2023); RAG (2017); Boersheim et al. (2019)"
        },
        "L80 (API 5CT)": {
            "result": "Validated",
            "condition": "Field & Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Maintained mechanical integrity",
            "failure_mode": "Slight ductility reduction; no cracking",
            "test_conditions": "Exposed to pure H₂ & blends",
            "time": "1000 h",
            "other_contaminants": "Sour gas",
            "h2_percentage": "100% / 10%",
            "pressure": "100–200",
            "temperature": "40–100",
            "test_type": "Field & Laboratory",
            "yield": "765",
            "source": "HyStories (Loder, 2023); Vallourec (2023); Iorio et al. (2023); Trautmann (2020); RAG (2017)"
        },
        "N80 (API 5CT)": {
            "result": "Validated",
            "condition": "Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Ultimate tensile strength unaffected",
            "failure_mode": "Surface corrosion only",
            "test_conditions": "Static exposure test",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "100%",
            "pressure": "100",
            "temperature": "100",
            "test_type": "Laboratory",
            "yield": "689",
            "source": "Boersheim et al. (2019)"
        },
        "P110 (API 5CT)": {
            "result": "Not validated",
            "condition": "Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Most affected by H₂; lower ductility",
            "failure_mode": "Hydrogen embrittlement; reduced toughness",
            "test_conditions": "Pure H₂ exposure",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100%",
            "pressure": "100",
            "temperature": "100",
            "test_type": "Laboratory",
            "yield": "758–862",
            "source": "Vallourec (2023); Trautmann (2020); Iorio et al. (2023); RAG (2017)"
        },
        "T95 (API 5CT)": {
            "result": "Validated but slight effect on steel",
            "condition": "Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Minor ductility loss; integrity retained",
            "failure_mode": "No major HE or cracking",
            "test_conditions": "Electrochemical test",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "Hydrogen-rich",
            "pressure": "-",
            "temperature": "-",
            "test_type": "Laboratory",
            "yield": "655",
            "source": "Iorio et al. (2023)"
        },
        "42CrMo4 (QT/QTT)": {
            "result": "Not validated",
            "condition": "Lab, 100C,100bar, 100%H2 1000h exposure",
            "final_state": "Below embrittlement threshold",
            "failure_mode": "Prone to HE (martensitic)",
            "test_conditions": "High-pressure H₂ exposure",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "Hydrogen-rich",
            "pressure": "-",
            "temperature": "-",
            "test_type": "Laboratory",
            "yield": ">1000",
            "source": "RAG (2017); Trautmann (2020)"
        },
        "P235": {
            "result": "Validated",
            "condition": "Field (Pilot), 10% H2",
            "final_state": "Performed well under blended gas",
            "failure_mode": "None reported",
            "test_conditions": "Casing steel in reuse well",
            "time": "-",
            "other_contaminants": "Brine / NG mixture",
            "h2_percentage": "10% H₂ + 90% NG",
            "pressure": "-",
            "temperature": "-",
            "test_type": "Field (Pilot)",
            "yield": "235",
            "source": "RAG (2017)"
        },
        "L360": {
            "result": "Validated",
            "condition": "Field (Pilot), 10% H2",
            "final_state": "Maintained integrity",
            "failure_mode": "None reported",
            "test_conditions": "Casing steel in reuse well",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "10% H₂ + 90% NG",
            "pressure": "-",
            "temperature": "-",
            "test_type": "Field (Pilot)",
            "yield": "360",
            "source": "RAG (2017)"
        },
        "AISI 316 (stainless) (Cr 16-18%, Ni 10-14%, Mb 2-3%)": {
            "result": "Validated, but slight effect on steel",
            "condition": "—",
            "final_state": "High H₂ uptake but resistant",
            "failure_mode": "Not tested in this report",
            "test_conditions": "Discussed theoretically",
            "time": "-",
            "other_contaminants": "-",
            "h2_percentage": "-",
            "pressure": "-",
            "temperature": "-",
            "test_type": "-",
            "yield": "-",
            "source": "Trautmann et al 2020"
        },
        "IN718 (Ni-base superalloy)": {
            "result": "Not validated",
            "condition": "Field, 42C, 200bar, 100%H2, 11months",
            "final_state": "High hydrogen trapping tendency",
            "failure_mode": "None reported, higher uptake",
            "test_conditions": "Part of alloy sample batch",
            "time": "11 months",
            "other_contaminants": "-",
            "h2_percentage": "100%",
            "pressure": "200",
            "temperature": "42",
            "test_type": "Field",
            "yield": "-",
            "source": "HyStock (Roordink et al., 2025)"
        },
        "34CrMo4": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~115 MPa√m (meets ASME B31.12)",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Cylinder application",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "HAZ X65": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~90 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "-",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "BM X65": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~100 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Transport pipeline base metal",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "WM X65": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~95 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Transport pipeline weld metal",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "BM X80": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~85 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Transport pipeline base metal",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "VM55W": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~75 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Pipe containment",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "VM80W": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~90 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Underground storage",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "VM80S": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~95 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Underground storage",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "VM95SS": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~100 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Underground storage",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
        "VM110SS": {
            "result": "Validated, higher than required to comply to standards",
            "condition": "Laboratory,vallourec steel, 100% H2, 1000h",
            "final_state": "KIH ~105 MPa√m",
            "failure_mode": "KIH higher han required to comply to standards",
            "test_conditions": "Underground storage",
            "time": "1000 h",
            "other_contaminants": "-",
            "h2_percentage": "100% H₂",
            "pressure": "-",
            "temperature": "Room temperature",
            "test_type": "Laboratory",
            "yield": "-",
            "source": "Vallourec (2023)"
        },
    }

    cell_1 = mapping[material]["result"]
    cell_2 = mapping[material]["condition"]
    cell_3 = mapping[material]["final_state"]
    cell_4 = mapping[material]["failure_mode"]
    cell_5 = mapping[material]["test_conditions"]
    cell_6 = mapping[material]["time"]
    cell_7 = mapping[material]["h2_percentage"]
    cell_8 = mapping[material]["pressure"]
    cell_9 = mapping[material]["temperature"]
    cell_10 = mapping[material]["test_type"]
    cell_11 = mapping[material]["yield"]
    cell_12 = mapping[material]["source"]
    return (
        cell_1,
        cell_2,
        cell_3,
        cell_4,
        cell_6,
        cell_7,
        cell_8,
        cell_9,
        cell_10,
        cell_11,
        cell_12
    )
