from dash import dcc, html
import dash_bootstrap_components as dbc

tab_intro = dcc.Tab(
        label="Intro",
        value="tab-intro",
        children=[
            html.Br(),
            html.Br(),
            html.Br(),

            dcc.Markdown(
                """
                ### **HyTROS Screening Framework Tool**
                #### Reusing wells for Underground Hydrogen Storage (UHS)
                """,
                style={"textAlign": "left"}
            ),
            
            html.Br(),

            dcc.Markdown(
                """
                This web-based screening tool supports the assessment of well reusability for underground hydrogen storage (UHS) in depleted gas reservoirs.
                It was developed under Sub-task 5.3 of GroenvermogenNL WP2 R&D HyTROS: Hydrogen Transport, Offshore and Storage project.

                The tool enables a structured and transparent screening of wells, highlighting expected mitigation severity and guiding further 
                engineering evaluation. The technical requirements and risks associated with well reuse for UHS were reviewed and documented in
                 Deliverable D5.3.1. These outcomes formed the basis for the screening methodology which was further developed in close collaboration 
                 with industry partners through technical discussions and dedicated workshops. The framework was tested using case studies based on 
                 real well data from candidate wells for pilot UHS projects in the Netherlands, supporting validation of the approach.

                 **Tool supporting project documentation:**
                 - D5.3.1 – Technical requirements and risks for well reuse in UHS: [TBD link or download option]
                 - D5.3.2 – Well reuse screening framework and case studies: [TBD link or download option]

                 
                 
                """,
                style={"textAlign": "left"}
            ),
            
            html.Br(),
            
            dcc.Markdown(
                """
                **Acknowledgements**

                 The development and validation of this tool were carried out in collaboration with HyTROS sub-task 5.3 project partners
                  who contributed expertise, data, and feedback.
                """,
                style={"textAlign": "left"}
            ),

            html.Img(
                src="/assets/partners.png",  # put image inside assets folder
                style={"width": "50%", "height": "auto", "textAlign": "center"}
            ),
            
            html.Br(),
        ]
    )