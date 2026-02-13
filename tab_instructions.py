from dash import dcc

tab_instructions = dcc.Tab(
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
        ]
    )