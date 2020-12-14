import plotly.express as px
import pandas as pd


def show_map(data):
    """Shows the map with the exact location of
       the query and that of the requested IP.
    """
    fig = px.scatter_mapbox(pd.DataFrame(data=data),
                            lat="lat",
                            lon="lon",
                            text="IP",
                            color_discrete_sequence=["blue"],
                            zoom=3,
                            height=1200)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.show()
