
import plotly.express as px

data = {'lat':[45.5, 54.4],
        'lon':[12.3, 17.9]}


fig = px.scatter_mapbox(data, lat="lat", lon="lon", color_discrete_sequence=["blue"], zoom=3, height=800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()