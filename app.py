import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(layout="wide")

st.title("Mapa de Calor: Chile")

# Generar datos de ejemplo con coordenadas dentro de Chile
data = pd.DataFrame({
    "lat": [-33.45, -34.61, -37.45, -23.65, -41.47],
    "lon": [-70.66, -71.61, -72.95, -70.40, -72.94],
    "intensidad": [10, 50, 80, 30, 100]
})

# Mostrar tabla de datos
st.subheader("Datos de Puntos")
st.dataframe(data)

# Crear el mapa de calor
st.subheader("Visualización de Mapa de Calor")
heatmap_layer = pdk.Layer(
    "HeatmapLayer",
    data=data,
    get_position="[lon, lat]",
    get_weight="intensidad",
    radiusPixels=60,
)

view_state = pdk.ViewState(
    latitude=-35.0,
    longitude=-71.0,
    zoom=4,
    pitch=40,
)

r = pdk.Deck(
    layers=[heatmap_layer],
    initial_view_state=view_state,
    tooltip={"text": "Intensidad: {intensidad}"},
)

st.pydeck_chart(r)
