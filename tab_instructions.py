from dash import dcc, html

tab_instructions = dcc.Tab(
    label="Instructions",
    value="tab-how",
    children=[
        html.Br(),

        html.Br(),

        dcc.Markdown(
            """
            #### Screening approach

            The screening is performed in two steps:

            1. **Well design – pre-screening:**
            A high-level review of well construction and operational aspects.

            2. **Well integrity – detailed screening:**
            A detailed assessment of well barrier elements (WBEs).


            For each step, a set of qualitative criteria (questions) is defined. Criteria are answered as *Yes*, *No*, or *Unknown*.

            For Well Integrity, responses reflect whether each WBE:
            - is Qualified / Fit-for-Service (FFS), and
            - demonstrates material compatibility

            Material compatibility assessments are based on the *Material Compatibility* tab.

            For non-retrievable WBEs, both Qualified / FFS and Material Compatibility must be positive. If either is not met, 
            the required mitigation is classified as Severe.

            For retrievable WBEs, if either criterion is not positive, the required mitigation is classified as Moderate.

            The user then selects the impact level, reflecting the consequences for operations should the identified issues not 
            be addressed. Definitions and guidance are provided in the Criteria Sheet.
            """,
            style={"textAlign": "left"}
        ),

        html.Br(),

        dcc.Markdown(
            """
            #### Results presentation

            Results are presented using a risk matrix that plots mitigation requirement against impact. While conventional risk 
            matrices are typically based on probability and consequence, the HyTROS framework focuses on identifying the expected 
            level of remediation or mitigation, weighted by the potential operational impact if issues are not addressed in time.
            """
        )
    ]
)

