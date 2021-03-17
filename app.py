
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from pydeck.types import String
import math
from ast import literal_eval

@st.cache
def load_data():
    dtype = {"diff_" + str(year): np.int64 for year in range(2001,2020)}
    dtype['lat'] = np.float64
    dtype['lon'] = np.float64
    data =  pd.read_csv('data/cities.csv', dtype=dtype)
    for year in range(2002,2020):
        data['color_'+str(year)] = data['color_'+str(year)].apply(literal_eval)
        data['abs_'+str(year)] = data['diff_'+str(year)].abs().apply(np.log2)
    return data

data = load_data()

st.title("Map of cities of Canada")
st.write(data)
year = st.slider("Year", min_value=2002, max_value=2020, value=2002, step=1)
r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state = pdk.ViewState(
        latitude = 49.89,
        longitude = -97.13,
        zoom = 3,
        pitch =  0,
    ),
    layers=[pdk.Layer(
        "ScatterplotLayer",
        data,
        opacity=0.5,
        get_position=["lon", "lat"],
        get_radius="abs_" + str(year) + " * 3000",
        get_fill_color="color_" + str(year),
        pickable=True,
    )],
    tooltip={"text": "{city_name}"},
)
st.pydeck_chart(r)

