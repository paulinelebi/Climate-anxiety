

def get_provincial_climate_summary(location):
    data = {
        "British Columbia - Vancouver": {
            "2020_temp": 11.2,
            "2050_temp": 13.8,
            "2020_hot_days": 12,
            "2050_hot_days": 28,
            "top_threats": ["Wildfire smoke", "Heat domes", "Air quality"]
        },
        "British Columbia - Interior": {
            "2020_temp": 7.8,
            "2050_temp": 10.4,
            "2020_hot_days": 16,
            "2050_hot_days": 40,
            "top_threats": ["Forest fires", "Drought", "Water stress"]
        },
        "Alberta - Calgary": {
            "2020_temp": 4.6,
            "2050_temp": 7.2,
            "2020_hot_days": 6,
            "2050_hot_days": 21,
            "top_threats": ["Drought", "Thunderstorms", "Economic transition"]
        },
        "Alberta - Edmonton": {
            "2020_temp": 3.9,
            "2050_temp": 6.6,
            "2020_hot_days": 5,
            "2050_hot_days": 19,
            "top_threats": ["Urban flooding", "Air quality", "Fire risk"]
        },
        "Saskatchewan - Regina": {
            "2020_temp": 3.7,
            "2050_temp": 6.3,
            "2020_hot_days": 8,
            "2050_hot_days": 22,
            "top_threats": ["Crop yield decline", "Heat stress", "Drought"]
        },
        "Saskatchewan - Saskatoon": {
            "2020_temp": 3.5,
            "2050_temp": 6.1,
            "2020_hot_days": 9,
            "2050_hot_days": 24,
            "top_threats": ["Extreme heat", "Pest shifts", "Agricultural volatility"]
        },
        "Manitoba - Winnipeg": {
            "2020_temp": 3.2,
            "2050_temp": 6.1,
            "2020_hot_days": 9,
            "2050_hot_days": 25,
            "top_threats": ["Floods", "Winter melt", "Heat"]
        },
        "Ontario - Toronto": {
            "2020_temp": 9.1,
            "2050_temp": 11.8,
            "2020_hot_days": 18,
            "2050_hot_days": 42,
            "top_threats": ["Urban flooding", "Extreme heat", "Infrastructure stress"]
        },
        "Ontario - Ottawa": {
            "2020_temp": 6.8,
            "2050_temp": 9.5,
            "2020_hot_days": 13,
            "2050_hot_days": 35,
            "top_threats": ["Flash floods", "Snow-to-rain shift", "Heat waves"]
        },
        "Ontario - North": {
            "2020_temp": 1.5,
            "2050_temp": 4.2,
            "2020_hot_days": 2,
            "2050_hot_days": 8,
            "top_threats": ["Permafrost melt", "Invasive species", "Transportation disruption"]
        },
        "Quebec - Montreal": {
            "2020_temp": 7.4,
            "2050_temp": 10.2,
            "2020_hot_days": 14,
            "2050_hot_days": 34,
            "top_threats": ["Ice storms", "Heat waves", "Stormwater overflow"]
        },
        "Quebec - Quebec City": {
            "2020_temp": 5.9,
            "2050_temp": 8.7,
            "2020_hot_days": 10,
            "2050_hot_days": 26,
            "top_threats": ["River flooding", "Extreme snowmelt", "Coastal erosion"]
        },
        "New Brunswick": {
            "2020_temp": 5.7,
            "2050_temp": 7.9,
            "2020_hot_days": 6,
            "2050_hot_days": 18,
            "top_threats": ["Sea level rise", "Forest pests", "Storm damage"]
        },
        "Nova Scotia - Halifax": {
            "2020_temp": 6.3,
            "2050_temp": 8.5,
            "2020_hot_days": 5,
            "2050_hot_days": 15,
            "top_threats": ["Sea level rise", "Storm surge", "Infrastructure erosion"]
        },
        "Prince Edward Island": {
            "2020_temp": 6.0,
            "2050_temp": 8.3,
            "2020_hot_days": 4,
            "2050_hot_days": 14,
            "top_threats": ["Coastal erosion", "Fisheries disruption", "Saltwater intrusion"]
        },
        "Newfoundland and Labrador": {
            "2020_temp": 4.0,
            "2050_temp": 6.2,
            "2020_hot_days": 1,
            "2050_hot_days": 5,
            "top_threats": ["Storm surge", "Fishery instability", "Infrastructure degradation"]
        },
        "Northern Territories": {
            "2020_temp": -2.0,
            "2050_temp": 1.5,
            "2020_hot_days": 0,
            "2050_hot_days": 2,
            "top_threats": ["Permafrost thaw", "Ecosystem shifts", "Arctic fires"]
        }
