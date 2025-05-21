import streamlit as st
import base64

from modules.climate_data import get_climate_trend
from modules.economic_risk import get_sector_risk
from modules.anxiety_model import calculate_anxiety_score
from modules.visuals import plot_temperature_trend, show_climate_map
from modules.sector_actions import get_sector_actions
from modules.location_profiles import get_canadian_provinces, get_regional_questions, get_local_resources
from modules.canada_climate_summary import get_provincial_climate_summary

# --- Set page ---
st.set_page_config(page_title="🌅 Climate Vulnerability Score", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: transparent;
    }
    video.bgvid {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.15;
        object-fit: cover;
    }
    </style>
    <video class="bgvid" autoplay muted loop>
        <source src="https://www.videvo.net/videvo_files/converted/2015_08/preview/Spinning_Earth_Loop.mp428825.webm" type="video/webm">
    </video>
""", unsafe_allow_html=True)

# --- Audio helper ---
def add_bg_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)

add_bg_audio("611610__djscreechingpossum__creepy-bioship-ambiance.mp3")

# --- Style ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Playfair Display', serif;
    background: linear-gradient(to bottom right, #ffecd2, #fcb69f);
    color: #2f2f2f;
}

.block-container {
    padding: 2rem 3rem;
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 18px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    color: #b84d72;
}

.stButton>button {
    background-color: #ffcad4;
    color: #3e3e3e;
    font-weight: bold;
    border-radius: 30px;
    border: none;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
}

.metric-container {
    padding: 1rem;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.3);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<h1 style='text-align: center;'>Climate Vulnerability Score</h1>
<p style='text-align: center; font-size: 20px;'>Understand your risks. Receive support. Take action.</p>
<blockquote style='text-align: center; font-style: italic;'>“In the depth of winter, I finally learned that within me there lay an invincible summer.” — Albert Camus</blockquote>
""", unsafe_allow_html=True)

# --- Input Form ---
name = st.text_input("🧍‍♀️ What’s your name?", value="Solenne")
age = st.slider("📆 Your age", 15, 80, 25)
location = st.selectbox("🌎 Where in Canada do you live?", get_canadian_provinces())
sector = st.selectbox("💼 Your work or study area", [
    "Energy", "Education", "Healthcare", "Finance", "Climate Research",
    "Technology", "Manufacturing", "Tourism", "Agriculture", "Not working", "Student"
])
stress = st.slider("📊 Daily stress level", 1, 10, 5)
support = st.slider("👥 Community support feeling", 1, 10, 5)
financial_security = st.slider("💸 Financial security feeling", 1, 10, 5)
future_agency = st.slider("🕊️ Control over your future", 1, 10, 5)
climate_news = st.select_slider("📰 How often do you follow climate news?", ["Never", "Sometimes", "Daily", "Constantly"])
has_experienced_disaster = st.radio("🌪️ Experienced a climate disaster?", ["Yes", "No"])

st.markdown("### 🌍 Regional Questions")
responses = [st.radio(q, ["Yes", "No"]) for q in get_regional_questions(location)]

# --- Run Model ---
if st.button("✨ Analyze My Score"):
    region = location.split(" - ")[0]
    summary_data = get_provincial_climate_summary(location)
    sector_risk = get_sector_risk(sector)
    anxiety_score = calculate_anxiety_score(
        age, region, sector_risk, stress, climate_news,
        has_experienced_disaster, support, financial_security, future_agency
    )

    st.session_state.update({
        "name": name, "age": age, "location": location, "sector": sector,
        "stress": stress, "support": support, "financial_security": financial_security,
        "future_agency": future_agency, "climate_news": climate_news,
        "has_experienced_disaster": has_experienced_disaster, "responses": responses,
        "region": region, "sector_risk": sector_risk,
        "anxiety_score": anxiety_score, "summary_data": summary_data
    })

# --- Results ---
if "anxiety_score" in st.session_state:
    st.markdown("## 🌸 Your Results")
    d = st.session_state.summary_data

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌡️ Climate Outlook")
        st.metric("2020 Avg Temp", f"{d['2020_temp']}°C")
        st.metric("2050 Projection", f"{d['2050_temp']}°C")
        st.metric("Hot Days (2020)", f"{d['2020_hot_days']} days")
        st.metric("Hot Days (2050)", f"{d['2050_hot_days']} days")

    with col2:
        st.subheader("💼 Sector Risk")
        st.metric("Risk", f"{st.session_state.sector_risk}/10")
        st.subheader("🧠 Anxiety Score")
        st.metric("Score", f"{st.session_state.anxiety_score}/100")

    with col3:
        st.subheader("🔍 Regional Threats")
        for t in d["top_threats"]:
            st.markdown(f"- {t}")

    st.markdown("### 🌱 What You Can Do")
    for rec in get_sector_actions(st.session_state.sector):
        st.markdown(f"- {rec}")

    st.markdown(f"### 📚 Resources in {st.session_state.location}")
    for r in get_local_resources(st.session_state.location):
        st.markdown(f"- {r}")

    with st.expander("📘 Methodology"):
        st.markdown("""
        - Canadian climate data from Climate Atlas and Environment Canada.
        - Score = local climate exposure + sectoral risk + resilience factors.
        - Resources curated to support adaptive capacity by region.
        """)
