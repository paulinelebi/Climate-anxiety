# modules/visuals.py

import plotly.graph_objs as go
import streamlit as st
import folium
from streamlit_folium import st_folium

# Province-specific colors
REGION_COLORS = {
    "British Columbia": "#FF6F61",
    "Alberta": "#6B5B95",
    "Ontario": "#88B04B",
    "Quebec": "#F7CAC9",
    "Manitoba": "#92A8D1",
    "Nova Scotia": "#955251",
    "Default": "#3F72AF"
}

def plot_temperature_trend(region):
    years = list(range(2020, 2055, 5))
    temp_paths = {
        "British Columbia": [11.2, 11.7, 12.3, 12.9, 13.4, 13.8, 14.0],
        "Ontario": [9.1, 9.7, 10.2, 10.8, 11.3, 11.8, 12.0],
        "Quebec": [7.4, 8.0, 8.6, 9.3, 9.8, 10.2, 10.5],
        "Alberta": [4.6, 5.1, 5.6, 6.2, 6.8, 7.2, 7.4]
    }
    temps = temp_paths.get(region, [8.0 + 0.2 * i for i in range(len(years))])
    color = REGION_COLORS.get(region, REGION_COLORS["Default"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=temps, mode='lines+markers', name='Projected Temp',
        line=dict(color=color, width=3),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title=f"Projected Avg Temperature in {region} (2020–2050)",
        xaxis_title="Year",
        yaxis_title="Temperature (°C)",
        template="plotly_white",
        height=400
    )
    return fig


def show_climate_map(region):
    region_coords = {
        "British Columbia": [49.25, -123.1],
        "Alberta": [51.05, -114.07],
        "Ontario": [43.7, -79.4],
        "Quebec": [45.5, -73.6],
        "Manitoba": [49.9, -97.14],
        "Nova Scotia": [44.65, -63.57]
    }
    latlon = region_coords.get(region, [56.1304, -106.3468])

    m = folium.Map(location=latlon, zoom_start=5, tiles="CartoDB positron")
    folium.CircleMarker(
        location=latlon,
        radius=10,
        color=REGION_COLORS.get(region, "#3F72AF"),
        fill=True,
        fill_color=REGION_COLORS.get(region, "#3F72AF"),
        fill_opacity=0.6,
        popup=f"{region} center"
    ).add_to(m)

    st.markdown(f"**📍 Approximate regional center for {region}:**")
    st_folium(m, width=700, height=400)
