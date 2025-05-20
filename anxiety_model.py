def calculate_anxiety_score(age, region, sector_risk, stress, news_exposure,
                            experienced_disaster, support, financial_security, future_agency):
    region_score = {
        "British Columbia": 25, "Alberta": 30, "Ontario": 20,
        "Quebec": 22, "Manitoba": 28, "Nova Scotia": 26
    }.get(region, 20)

    age_score = max(0, (80 - age) / 80) * 40
    sector_score = sector_risk * 2
    stress_score = stress * 2
    news_score = {"Never": 0, "Sometimes": 5, "Daily": 10, "Constantly": 15}[news_exposure]
    disaster_score = 15 if experienced_disaster == "Yes" else 0
    resilience_score = (support + financial_security + future_agency) / 3 * 2

    raw = region_score + age_score + sector_score + stress_score + news_score + disaster_score
    total = raw - resilience_score
    return round(min(max(total, 0), 100))
