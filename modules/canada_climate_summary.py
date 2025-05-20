

def get_provincial_climate_summary(location):
    data = {
        "British Columbia - Vancouver": {
            "2020_temp": 11.2,
            "2050_temp": 13.8,
            "2020_hot_days": 12,
            "2050_hot_days": 28,
            "top_threats": ["Wildfire smoke", "Heat domes", "Air quality"]
        },
        "Alberta - Calgary": {
            "2020_temp": 4.6,
            "2050_temp": 7.2,
            "2020_hot_days": 6,
            "2050_hot_days": 21,
            "top_threats": ["Drought", "Thunderstorms", "Economic transition"]
        },
        "Ontario - Toronto": {
            "2020_temp": 9.1,
            "2050_temp": 11.8,
            "2020_hot_days": 18,
            "2050_hot_days": 42,
            "top_threats": ["Urban flooding", "Extreme heat", "Infrastructure stress"]
        },
        "Quebec - Montreal": {
            "2020_temp": 7.4,
            "2050_temp": 10.2,
            "2020_hot_days": 14,
            "2050_hot_days": 34,
            "top_threats": ["Ice storms", "Heat waves", "Stormwater overflow"]
        },
        "Manitoba - Winnipeg": {
            "2020_temp": 3.2,
            "2050_temp": 6.1,
            "2020_hot_days": 9,
            "2050_hot_days": 25,
            "top_threats": ["Floods", "Winter melt", "Heat"]
        },
        "Nova Scotia - Halifax": {
            "2020_temp": 6.3,
            "2050_temp": 8.5,
            "2020_hot_days": 5,
            "2050_hot_days": 15,
            "top_threats": ["Sea level rise", "Storm surge", "Infrastructure erosion"]
        }
    }
    return data.get(location, {
        "2020_temp": None,
        "2050_temp": None,
        "2020_hot_days": None,
        "2050_hot_days": None,
        "top_threats": ["Localized risk data not available"]
    })
