import pandas as pd

def get_climate_trend(region):
    trends = {
        "North America": "Projected 2.3°C increase by 2100 under current policies.",
        "Europe": "1.9°C increase by 2100 with some variability.",
        "Asia": "3.0°C increase and high flood risk.",
        "Africa": "2.7°C increase with major drought risks."
    }

    years = list(range(2000, 2026))
    co2_levels = {
        "North America": [370 + 1.5 * i for i in range(26)],
        "Europe": [370 + 1.4 * i for i in range(26)],
        "Asia": [370 + 1.8 * i for i in range(26)],
        "Africa": [370 + 1.6 * i for i in range(26)],
    }

    df = pd.DataFrame({"Year": years, "CO2_ppm": co2_levels[region]})
    df = df.set_index("Year")

    return trends[region], df
