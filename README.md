Climate Vulnerability/Anxiety Simulator

This project is a web app that helps people in Canada understand how climate change might affect their local area - and how that connects to feelings of anxiety or uncertainty about the future. 
It’s built around real climate projections (like temperature rise and extreme heat days), plus some reflective questions that generate a “climate anxiety score.” 
Based on that, the app shows relevant risks, local data, and ways to take action.

The goal is to make climate change feel more personal (to inspire action and help people understand how it will affect everyone), 
and also about translating emotion into insight - doing feels more managable than just feeling anxious or scared. 

The app uses simple visuals, ambient sounds, and a calm layout to make the experience user-friendly, immersive and interactive, but also not too overwhelming.

Structure
app.py – main Streamlit interface
modules/ – contains the app’s logic and backend structure:
anxiety_model.py – scoring logic for anxiety assessment
canada_climate_summary.py – combines 2020 and 2050 regional projections
climate_data.py – reads and processes raw climate datasets
economic_risk.py – links economic exposure to climate vulnerability
location_profiles.py – defines key climate traits by region
map_compare.py – generates interactive climate maps
sector_actions.py – suggests sector-specific actions users can take
visuals.py – handles visual theming and layout
pastcode/ – archived or older logic (e.g. earlier summary scripts)

Requirements & setup
You’ll need to manually add:
- Climate data CSVs to a data/ folder (not included in repo)
- Background .mp4 video and .mp3 audio files in an assets/ folder

Then:
bash
Copy
Edit
pip install -r requirements.txt
streamlit run app.py

Still in progress, not all features (like saving scores or user history) are implemented yet. Feedback welcome!
