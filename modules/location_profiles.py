
from modules.canada_climate_summary import climate_data_dict

def get_canadian_provinces():
    return list(climate_data_dict.keys())

def get_regional_questions(location):
    if "British Columbia" in location:
        return [
            "Have you or your family been affected by wildfire smoke in the past 3 years?",
            "Do you feel your local area is prepared for heat domes or summer air quality alerts?"
        ]
    elif "Ontario" in location:
        return [
            "Have you noticed changes in seasonal flooding or storm intensity where you live?",
            "Do you feel provincial policies in Ontario are addressing climate adaptation fast enough?"
        ]
    elif "Quebec" in location:
        return [
            "Has extreme cold or storm disruption affected your work or mobility?",
            "Are climate communication resources available in your preferred language?"
        ]
    elif "Alberta" in location:
        return [
            "Has your region experienced economic instability due to energy transition policies?",
            "How aware are you of renewable initiatives in your local community?"
        ]
    else:
        return [
            "Do you feel your community has enough support systems during climate-related events?",
            "Are you confident in local climate planning efforts?"
        ]

def get_local_resources(location):
    base_resources = [
        "🌐 [Climate Atlas of Canada](https://climateatlas.ca)",
        "📰 [The Narwhal](https://thenarwhal.ca) - Independent climate journalism",
        "🧭 [Re.Climate](https://reclimate.ca) - Climate communications think tank"
    ]

    if "British Columbia" in location:
        return base_resources + [
            "🌲 [BC Wildfire Service Alerts](https://www2.gov.bc.ca/gov/content/safety/wildfire-status)",
            "🏘️ [Fraser Basin Council](https://www.fraserbasin.bc.ca/) - Resilience programs"
        ]
    elif "Ontario" in location:
        return base_resources + [
            "🌧️ [Ontario Flood Map](https://www.ontario.ca/page/flood-forecasting-and-warning-program)",
            "📘 [Clean Air Partnership](https://cleanairpartnership.org/)"
        ]
    elif "Quebec" in location:
        return base_resources + [
            "🔎 [Ouranos Consortium](https://www.ouranos.ca/en/) - Climate science for Quebec",
            "🎧 [Unpointcinq](https://unpointcinq.ca) - Climate podcast & news (French)"
        ]
    else:
        return base_resources + [
            "📋 [Natural Resources Canada](https://www.nrcan.gc.ca/) - National risk maps and resources"
        ]
