from dash import Dash, html, dcc, callback, Output, Input, MATCH
from tab_well_design import tab_well_design
from tab_instructions import tab_instructions
from tab_well_integrity import tab_well_integrity

app = Dash(__name__)






# ---------- Layout ----------
app.layout = html.Div(
    style={"maxWidth": "1500px", "margin": "24px auto", "fontFamily": "system-ui"},
    children=[
        html.H2("HyTROS Screening Framework"),

        # Shared state between tabs
        dcc.Store(id="app-state", storage_type="memory"),

        dcc.Tabs(
            id="tabs",
            value="well-integrity",
            children=[
                tab_instructions,

                tab_well_design,

                tab_well_integrity

            ]
        )
    ]
)












if __name__ == "__main__":
    app.run(debug=True)