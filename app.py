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
    .main { background-color: #f5f5f5; }
    .block-container { padding: 2rem 2rem 2rem 2rem; }
    h1, h2, h3 { color: #3b3b3b; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🌿 Climate Anxiety Score</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Understand your risks. Receive support. Take action.</p>", unsafe_allow_html=True)
st.markdown("---")

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

if "anxiety_score" in st.session_state:
    st.markdown("## 📈 Your Results")

    with st.container():
        st.subheader("🌡️ Local Climate Outlook")
        d = st.session_state.summary_data
        st.metric("Avg Temp in 2020", f"{d['2020_temp']}°C")
        st.metric("Avg Temp in 2050", f"{d['2050_temp']}°C")
        st.metric("Hot Days Now", f"{d['2020_hot_days']} days/year")
        st.metric("Projected Hot Days 2050", f"{d['2050_hot_days']} days/year")
        st.markdown("**Top regional climate threats:**")
        for threat in d["top_threats"]:
            st.markdown(f"- {threat}")

    with st.container():
        st.subheader("💼 Sector Risk")
        st.metric("Risk Level", f"{st.session_state.sector_risk}/10")

    with st.container():
        st.subheader("🧠 Climate Anxiety Score")
        st.metric("Score", f"{st.session_state.anxiety_score}/100")
        st.markdown("### Contributing Factors")
        st.markdown("""
        - 📍 **Region**: Local exposure to climate stress
        - 💼 **Sector**: Transition vulnerability
        - 🧑 **Age**: Future horizon
        - 📰 **News exposure**, 🌪️ **Disaster history**
        - 👥 **Support**, 💸 **Security**, 🕊️ **Agency**
        """)

    with st.container():
        st.subheader("🌱 What You Can Do")
        for rec in get_sector_actions(st.session_state.sector):
            st.markdown(f"- {rec}")

    with st.container():
        st.subheader(f"📚 Resources in {st.session_state.location}")
        for r in get_local_resources(st.session_state.location):
            st.markdown(f"- {r}")

    with st.expander("📘 Methodology"):
        st.markdown("""
        - Canadian climate data based on summaries from Climate Atlas and Environment Canada.
        - Anxiety score blends physical exposure, job risk, psychological resilience.
        - Resources are curated per province to support literacy, planning, and community action.
        """)
