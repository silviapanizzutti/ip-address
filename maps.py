import plotly.graph_objects as go
import plotly.express as px
import pandas as pd # hover_name="City", hover_data=["State", "Population"]
def show_map(data):
    fig = px.scatter_mapbox(pd.DataFrame(data=data), lat="lat", lon="lon",
                        color_discrete_sequence=["fuchsia"], zoom=3, height=1200)
    fig = go.Figure(data=go.Scattergeo(
        lat = data["lat"],
        lon = data["lon"],
        mode = 'lines',
        line = dict(width = 2, color = 'blue'),
    ))

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.show()
