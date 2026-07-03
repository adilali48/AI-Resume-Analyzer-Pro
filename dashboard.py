import plotly.graph_objects as go


class Dashboard:

    def ats_gauge(self, score):

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,

                title={
                    "text": "ATS Score"
                },

                gauge={
                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "color": "green"
                    },

                    "steps": [

                        {
                            "range": [0, 40],
                            "color": "#ff4b4b"
                        },

                        {
                            "range": [40, 70],
                            "color": "#ffa500"
                        },

                        {
                            "range": [70, 100],
                            "color": "#00cc66"
                        }

                    ]
                }
            )
        )

        fig.update_layout(
            height=350,
            margin=dict(
                l=20,
                r=20,
                t=40,
                b=20
            )
        )

        return fig