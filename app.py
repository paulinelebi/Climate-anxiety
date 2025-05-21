import streamlit as st
from modules.climate_data import get_climate_trend
from modules.economic_risk import get_sector_risk
from modules.anxiety_model import calculate_anxiety_score
from modules.visuals import plot_temperature_trend, show_climate_map
from modules.sector_actions import get_sector_actions
from modules.location_profiles import get_canadian_provinces, get_regional_questions, get_local_resources
from modules.canada_climate_summary import get_provincial_climate_summary

import base64

st.set_page_config(page_title="🌍 Climate Anxiety Score", layout="wide")

# Load background audio
def add_bg_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )

add_bg_audio("611610__djscreechingpossum__creepy-bioship-ambiance.mp3")

# Apply custom styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(to bottom, #ffeef4, #fdf7fa);
    }

    .block-container {
        background: rgba(255, 255, 255, 0.75);
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    }

    h1, h2, h3 {
        color: #bf5f82;
    }

    .stButton>button {
        background-color: #f6c1d5;
        color: black;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    .fade-in {
        animation: fadeIn 1.5s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Header and quote
st.markdown("""
    <h1 style='text-align: center;'>🌿 Climate Anxiety Score</h1>
    <p style='text-align: center; font-size: 20px;'>Understand your risks. Receive support. Take action.</p>
    <blockquote style='text-align: center; font-style: italic; color: #7a4b54;'>
        "In the depth of winter, I finally learned that within me there lay an invincible summer." – Albert Camus
    </blockquote>
    <hr>
""", unsafe_allow_html=True)

# Input form
name = st.text_input("🧍‍♀️ What’s your name?", value="Solenne")
age = st.slider("📆 Your age", 15, 80, 25)
location = st.selectbox("🌎 Where in Canada do you live?", get_canadian_provinces())
sector = st.selectbox("💼 Your work or study area", [
    "Energy", "Education", "Healthcare", "Finance", "Climate Research",
    "Technology", "Manufacturing", "Tourism", "Agriculture", "Not working", "Student"])

stress = st.slider("📊 Daily stress level", 1, 10, 5)
support = st.slider("👥 Community support feeling", 1, 10, 5)
financial_security = st.slider("💸 Financial security feeling", 1, 10, 5)
future_agency = st.slider("🕊️ Control over your future", 1, 10, 5)

climate_news = st.select_slider("📰 How often do you follow climate news?", options=["Never", "Sometimes", "Daily", "Constantly"])
has_experienced_disaster = st.radio("🌪️ Experienced a climate disaster?", ["Yes", "No"])

custom_questions = get_regional_questions(location)
st.markdown("### 🌍 Regional Questions")
responses = [st.radio(q, ["Yes", "No"]) for q in custom_questions]

# Submit button
if st.button("✨ Analyze My Profile"):
    region = location.split(" - ")[0]
    summary_data = get_provincial_climate_summary(location)
    sector_risk = get_sector_risk(sector)
    anxiety_score = calculate_anxiety_score(
        age, region, sector_risk, stress, climate_news,
        has_experienced_disaster, support, financial_security, future_agency
    )

    st.session_state.update({
        "name": name,
        "age": age,
        "location": location,
        "sector": sector,
        "stress": stress,
        "support": support,
        "financial_security": financial_security,
        "future_agency": future_agency,
        "climate_news": climate_news,
        "has_experienced_disaster": has_experienced_disaster,
        "responses": responses,
        "region": region,
        "sector_risk": sector_risk,
        "anxiety_score": anxiety_score,
        "summary_data": summary_data
    })

# Results section
if "anxiety_score" in st.session_state:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌡️ Climate Outlook")
        d = st.session_state.summary_data
        st.metric("2020 Avg Temp", f"{d['2020_temp']}°C")
        st.metric("2050 Avg Temp", f"{d['2050_temp']}°C")
        st.metric("Hot Days Now", f"{d['2020_hot_days']} days/yr")
        st.metric("Hot Days in 2050", f"{d['2050_hot_days']} days/yr")

    with col2:
        st.subheader("💼 Sector Risk")
        st.metric("Risk Level", f"{st.session_state.sector_risk}/10")
        st.subheader("🧠 Climate Anxiety")
        st.metric("Score", f"{st.session_state.anxiety_score}/100")

    with col3:
        st.subheader("🌱 What You Can Do")
        for rec in get_sector_actions(st.session_state.sector):
            st.markdown(f"- {rec}")

    st.markdown("### 📚 Resources in your region")
    for r in get_local_resources(st.session_state.location):
        st.markdown(f"- {r}")

    with st.expander("📘 Methodology"):
        st.markdown("""
        - Canadian climate data from Climate Atlas & Environment Canada.
        - Risk is a combination of physical exposure, sector sensitivity, and personal resilience.
        - Resources curated by province to support adaptation and wellbeing.
        """)

    st.markdown('</div>', unsafe_allow_html=True)

