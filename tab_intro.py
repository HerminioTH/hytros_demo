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
                ### **HyTROS Screening Tool**
                #### Reusing wells for Underground Hydrogen Storage (UHS)
                """,
                style={"textAlign": "left"}
            ),
            
            html.Br(),

            # dcc.Markdown(
            #     """
            #     This web-based screening tool supports the assessment of well reusability for underground hydrogen storage (UHS) in depleted gas reservoirs.
            #     It was developed under Sub-task 5.3 of GroenvermogenNL WP2 R&D HyTROS: Hydrogen Transport, Offshore and Storage project.

            #     The tool enables a structured and transparent screening of wells, highlighting expected mitigation severity and guiding further 
            #     engineering evaluation. The technical requirements and risks associated with well reuse for UHS were reviewed and documented in
            #      Deliverable D5.3.1. These outcomes formed the basis for the screening methodology which was further developed in close collaboration 
            #      with industry partners through technical discussions and dedicated workshops. The framework was tested using case studies based on 
            #      real well data from candidate wells for pilot UHS projects in the Netherlands, supporting validation of the approach.

            #      **Tool supporting project documentation:**
            #      - D5.3.1 – Technical requirements and risks for well reuse in UHS: [TBD link or download option]
            #      - D5.3.2 – Well reuse screening framework and case studies: [TBD link or download option]

                 
                 
            #     """,
            #     style={"textAlign": "left"}
            # ),

            dcc.Markdown(
                """
                The HyTROS Well Screening Tool is a web-based research tool supporting the assessment of well reusability for underground hydrogen 
                storage (UHS) in depleted gas reservoirs. It was developed under Sub-task 5.3 of the GroenvermogenNL WP2 R&D project HyTROS: Hydrogen 
                Transport, Offshore and Storage. 

                The tool enables a structured and transparent screening of wells, indicating expected mitigation severity and supporting further 
                engineering evaluation. The methodology is based on work documented in Deliverable D5.3.1 and further developed in collaboration with 
                industry partners through technical discussions and workshops. The framework has been tested using case studies based on real well data 
                from candidate UHS sites in the Netherlands.

                **Supporting project documentation:**
                - D5.3.1 – Technical requirements and risks for well reuse in UHS
                - D5.3.2 – Well reuse screening framework and case studies

                **Disclaimer**

                This tool is developed as part of research activities under the GroenvermogenNL HyTROS project and is intended for screening and 
                research purposes only. It does not replace detailed engineering assessment. TNO and project partners do not guarantee the accuracy 
                or completeness of the results and accept no liability for decisions based on this tool.

                No input data provided to this tool is intended to be stored by TNO or the project partners; users should exercise their own 
                discretion when entering sensitive or confidential information. 

                **Funding**

                This work is part of the GroenvermogenNL programme. 

                **Contact**

                Vedran Zikovic – [vedran.zikovic@tno.nl](mailto:vedran.zikovic@tno.nl)
                 
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