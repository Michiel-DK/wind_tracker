import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

merged = pd.read_csv('data/merged.csv')

fig = go.Figure(px.scatter_mapbox(
    merged,
    lat="lat",
    lon="lon",
    color="speed",
    hover_data=["full_address", "speed", "deg", "gust"],
    animation_frame="time",
).update_layout(
    mapbox={"style": "carto-positron", "zoom":12}, margin={"l": 0, "r": 0, "t": 0, "b": 0},
    autosize=True
))

st.plotly_chart(fig)

st.markdown('Notes:')
st.markdown('Color change per windspeed (non-consistent scale)')
st.markdown('Direction possible but tricky to visualize')