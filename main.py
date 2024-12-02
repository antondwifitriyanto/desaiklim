import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium

# Judul aplikasi
st.title("Visualisasi Shapefile dengan Streamlit")

# Unggah file SHP
uploaded_file = st.file_uploader("Unggah file SHP (dengan file pendukung seperti .shx, .dbf, dll.)", type=["zip"])

if uploaded_file:
    # Simpan file SHP yang diunggah
    with open("temp.zip", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Baca file SHP
    gdf = gpd.read_file("zip://temp.zip")

    # Tampilkan GeoDataFrame
    st.write("Dataframe dari shapefile:")
    st.dataframe(gdf)

    # Visualisasi di peta dengan Folium
    m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=10)

    # Tambahkan GeoDataFrame ke peta
    folium.GeoJson(gdf).add_to(m)

    # Tampilkan peta di Streamlit
    st_folium(m, width=700, height=500)
