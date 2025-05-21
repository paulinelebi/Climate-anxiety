def get_provincial_climate_summary(location):
    data = {
        "British Columbia - Vancouver": {
            "2020_temp": 11.2, "2050_temp": 13.8,
            "2020_hot_days": 12, "2050_hot_days": 28,
            "top_threats": ["Wildfire smoke", "Heat domes", "Air quality"]
        },
        "British Columbia - Interior": {
            "2020_temp": 7.8, "2050_temp": 10.4,
            "2020_hot_days": 16, "2050_hot_days": 40,
            "top_threats": ["Forest fires", "Drought", "Water stress"]
        },
        # ... all other provinces ...
    }

    # Standardize the input (strip whitespace, make consistent case)
    location = location.strip()

    # Direct match
    if location in data:
        return data[location]

    # Try fuzzy match (e.g., allow user to input just "Vancouver" or "Toronto")
    for key in data:
        if location.lower() in key.lower():
            print(f"[INFO] Fuzzy-matched input '{location}' to key '{key}'")
            return data[key]

    # Log issue
    print(f"[WARN] Location '{location}' not found in climate summary data.")

    # Return safe default
    return {
        "2020_temp": "N/A",
        "2050_temp": "N/A",
        "2020_hot_days": "N/A",
        "2050_hot_days": "N/A",
        "top_threats": ["Data not available"]
    }
