# modules/map_compare.py

import streamlit as st
import folium
from streamlit_folium import st_folium

def show_click_to_compare_map():
    # Coordinates for each province
    province_coords = {
        "British Columbia": [53.7267, -127.6476],
        "Alberta": [53.9333, -116.5765],
        "Saskatchewan": [52.9399, -106.4509],
        "Manitoba": [53.7609, -98.8139],
        "Ontario": [50.0000, -85.0000],
        "Quebec": [52.0000, -71.7500],
        "New Brunswick": [46.5653, -66.4619],
        "Nova Scotia": [44.6820, -63.7443],
        "Prince Edward Island": [46.5107, -63.4168],
        "Newfoundland and Labrador": [53.1355, -57.6604],
        "Northern Territories": [64.8255, -124.8457]
    }

    # Climate risk scores out of 10
    climate_risks = {
        "British Columbia": 8.5,
        "Alberta": 7.2,
        "Saskatchewan": 6.8,
        "Manitoba": 6.5,
        "Ontario": 7.0,
        "Quebec": 6.9,
        "New Brunswick": 5.2,
        "Nova Scotia": 5.4,
        "Prince Edward Island": 5.0,
        "Newfoundland and Labrador": 4.8,
        "Northern Territories": 7.8
    }

    national_avg = round(sum(climate_risks.values()) / len(climate_risks), 1)

    st.markdown("### Climate Risk Across Canada")
    st.markdown("Click a province to compare its projected 2050 climate risk to the national average.")

    m = folium.Map(location=[56, -96], zoom_start=4, tiles='cartodbpositron')

    for province, coords in province_coords.items():
        risk = climate_risks.get(province, "N/A")
        comparison = (
            "above average" if risk > national_avg else
            "below average" if risk < national_avg else
            "equal to the national average"
        )
        popup = f"{province}<br>Risk Score: {risk}/10<br>This is {comparison} (National Avg: {national_avg})"

        folium.CircleMarker(
            location=coords,
            radius=9,
            popup=popup,
            tooltip=province,
            color='red' if risk > national_avg else 'green',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

    st_folium(m, width=750, height=500)
