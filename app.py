import streamlit as st
from modules.climate_data import get_climate_trend
from modules.economic_risk import get_sector_risk
from modules.anxiety_model import calculate_anxiety_score
from modules.visuals import plot_temperature_trend, show_climate_map
from modules.sector_actions import get_sector_actions
from modules.location_profiles import get_canadian_provinces, get_regional_questions, get_local_resources
from modules.canada_climate_summary import get_provincial_climate_summary

st.set_page_config(page_title="🌍 Do you have climate anxiety? The Climate Score Index: Find yours!", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to bottom right, #121212, #1e1e1e);
        color: #f0f0f0;
    }
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }
    h1, h2, h3 {
        color: #f4f4f4;
        font-weight: 600;
    }
    .stTextInput > div > div > input {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 8px;
    }
    .stSelectbox > div > div > div > div {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 8px;
    }
    .stSlider > div {
        color: #ffffff;
    }
    .stRadio > div {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center;'>🌿 Climate Anxiety Companion</h1>
<p style='text-align: center; font-size: 18px;'>Understand your risks. Receive support. Take action.</p>
<p style='text-align: center; font-style: italic; color: #aaa;'>"In the depth of winter, I finally learned that within me there lay an invincible summer." – Albert Camus</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
    <h1 style='text-align: center;'>🌿 Climate Anxiety Companion</h1>
    <p style='text-align: center; font-size: 18px;'>Understand your risks. Receive support. Take action.</p>
    <blockquote style="font-style:italic; font-size: 1.1rem; color: #555;">
        "In the depth of winter, I finally learned that within me there lay an invincible summer." – Albert Camus
    </blockquote>
    <hr>
""", unsafe_allow_html=True)

# --- Input Form ---
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

if st.button("Ready to see your score? Click here"):
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

if "anxiety_score" in st.session_state:
    st.markdown("## 📈 Your results")

    with st.container():
        st.subheader("🌡️ Local climate outlook")
        d = st.session_state.summary_data
        st.metric("Avg temp in 2020", f"{d['2020_temp']}°C")
        st.metric("Avg temp in 2050", f"{d['2050_temp']}°C")
        st.metric("Hot days (+30 degrees celsius) now", f"{d['2020_hot_days']} days/year")
        st.metric("Projected hot days 2050", f"{d['2050_hot_days']} days/year")
        st.markdown("**Top regional climate threats:**")
        for threat in d["top_threats"]:
            st.markdown(f"- {threat}")

    with st.container():
        st.subheader("💼 Sector risk")
        st.metric("Risk Level", f"{st.session_state.sector_risk}/10")

    with st.container():
        st.subheader("🧠 Climate anxiety score")
        st.metric("Score", f"{st.session_state.anxiety_score}/100")
        st.markdown("### Factors that contribute to your score:")
        st.markdown("""
        - 📍 **Region**: Local exposure to climate stress
        - 💼 **Sector**: Transition vulnerability
        - 🧑 **Age**: Future horizon
        - 📰 **News exposure**, 🌪️ **Disaster history**
        - 👥 **Support**, 💸 **Security**, 🕊️ **Agency**
        """)

    with st.container():
        st.subheader("🌱 So... what can you do?")
        for rec in get_sector_actions(st.session_state.sector):
            st.markdown(f"- {rec}")

    with st.container():
        st.subheader(f"📚 Please check out these resources in {st.session_state.location}")
        for r in get_local_resources(st.session_state.location):
            st.markdown(f"- {r}")

    with st.expander("📘 The methodology"):
        st.markdown("""
        - Canadian climate data based on summaries from Climate Atlas and Environment Canada.
        - Anxiety score blends physical exposure, job risk, psychological resilience.
        - Resources are curated per province to support literacy, planning, and community action.
        """)
