import streamlit as st
import folium
from streamlit_folium import st_folium

def show_click_to_compare_map():
    # Province center coordinates
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

    # Climate risk scores (out of 10)
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
        "Northern Territories": 7.8,
    }

    # Calculate national average
    national_avg = round(sum(climate_risks.values()) / len(climate_risks), 1)

    # Get user's selected province from session state
    user_location = st.session_state.get("location", "")
    user_province = user_location.split(" - ")[0] if " - " in user_location else user_location

    # Header
    st.markdown("### 🗺️ Climate Risk Across Canada")
    st.markdown("Click a province to compare its projected 2050 risk to the national average.")

    # Initialize folium map
    m = folium.Map(location=[56, -96], zoom_start=4, tiles="cartodbpositron")

    # Add each province as a circle marker
    for province, coords in province_coords.items():
        risk = climate_risks.get(province, "N/A")
        comparison = (
            "above average" if risk > national_avg else
            "below average" if risk < national_avg else
            "equal to the national average"
        )
        popup_html = f"""
        <div style="font-family: sans-serif; font-size: 14px;">
            <b>{province}</b><br>
            Risk Score: <b>{risk}/10</b><br>
            This is <i>{comparison}</i><br>
            (National Avg: {national_avg})
        </div>
        """

        # Highlight user's province
        is_user = user_province.strip().lower() == province.lower()
        color = (
            "darkred" if risk >= 8 else
            "orange" if risk >= 6 else
            "lightgreen"
        )
        radius = 11 if is_user else 7
        border_color = "black" if is_user else color

        folium.CircleMarker(
            location=coords,
            radius=radius,
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{province} (You)" if is_user else province,
            color=border_color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8
        ).add_to(m)

    # Display the map with full-width and no white space
    st.markdown("---")
    st_folium(m, height=520, use_container_width=True)

