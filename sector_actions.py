

def get_sector_actions(sector):
    actions = {
        "Energy": [
            "Support or join renewable projects in your region",
            "Advocate for grid modernization and sustainable energy policies"
        ],
        "Education": [
            "Incorporate sustainability and climate awareness into your curriculum",
            "Host community climate literacy workshops"
        ],
        "Healthcare": [
            "Promote climate-related health research and adaptation planning",
            "Support cooling centers or health equity planning during heatwaves"
        ],
        "Finance": [
            "Advocate for climate-aligned investment strategies",
            "Support green bonds or transition finance instruments"
        ],
        "Climate Research": [
            "Publish public-facing summaries of regional climate models",
            "Collaborate with policy-makers to localize action"
        ],
        "Technology": [
            "Help optimize data center sustainability",
            "Design tools to support individual and institutional decarbonization"
        ],
        "Manufacturing": [
            "Investigate low-carbon supply chain strategies",
            "Support product lifecycle analysis and eco-labeling"
        ],
        "Tourism": [
            "Promote local low-carbon travel options",
            "Design carbon-conscious visitor education initiatives"
        ],
        "Agriculture": [
            "Incorporate regenerative practices and water optimization",
            "Support local food systems and carbon soil storage awareness"
        ],
        "Student": [
            "Join a climate org or campus initiative",
            "Pitch climate-aware ideas in class or projects"
        ],
        "Not working": [
            "Volunteer with regional climate or resilience groups",
            "Educate yourself and others on local risks and resilience pathways"
        ]
    }
    return actions.get(sector, ["Explore sustainable behavior in your area of life."])