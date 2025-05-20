def get_sector_risk(sector):
    risk_map = {
        "Finance": 3,
        "Agriculture": 9,
        "Tech": 4,
        "Healthcare": 5,
        "Education": 6
    }
    return risk_map.get(sector, 5)
