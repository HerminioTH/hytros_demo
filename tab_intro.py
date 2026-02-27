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
                #### Welcome to HyTROS Screening Framework Tool
                """,
                style={"textAlign": "left"}
            ),
            
            html.Br(),

            dcc.Markdown(
                """
                This tool is intended to aid user decide whether a well can be repurposed for hydrogen operations. 
                It was developed within the project HyTROS...
                """,
                style={"textAlign": "left"}
            ),
            
            html.Br(),

            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            dcc.Markdown(
                                """
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
                                """,
                                style={"textAlign": "left"}
                            )
                        ],
                        title="User instructions",
                    )
                ],
                start_collapsed=True,
            )
        ]
    )