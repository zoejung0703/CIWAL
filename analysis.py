"""
analysis.py - Text-based visualization (ending + orientation analysis included)
"""

ORIENTATION_MAP = {
    "Efficiency-oriented": "Utilitarianism",
    "Happiness-oriented": "Welfarism",
    "Freedom-oriented": "Liberalism",
    "Equality-oriented": "Rawlsianism",
    "Sustainability-oriented": "Environmentalism"
}

def bar_line(name, value, desc, width=30):
    """Generate a text-based bar chart line"""
    filled = int((max(0, min(value, 100)) / 100) * width)
    bar = "█" * filled + " " * (width - filled)
    return f"{name:<15} '{value:>3}': 0 [{bar}] 100  ({desc})"

def interpret_metrics(m):
    """Return human-readable interpretations of metrics"""
    interp = {}
    if m["gdp"] > 100:
        interp["gdp"] = "Top OECD level, hyper growth"
    elif m["gdp"] > 70:
        interp["gdp"] = "Developed country average"
    elif m["gdp"] > 40:
        interp["gdp"] = "Middle-income level"
    else:
        interp["gdp"] = "Low-income, crisis"

    if m["happiness"] > 70:
        interp["happiness"] = "Highest in the world (Nordic level)"
    elif m["happiness"] > 50:
        interp["happiness"] = "Global average"
    elif m["happiness"] > 30:
        interp["happiness"] = "Warning: rising discontent"
    else:
        interp["happiness"] = "Collapse imminent, rebellion risk"

    if m["freedom"] > 70:
        interp["freedom"] = "Fully free society"
    elif m["freedom"] > 40:
        interp["freedom"] = "Partially free"
    else:
        interp["freedom"] = "Authoritarian, repressive"

    if m["inequality"] < 30:
        interp["inequality"] = "Highly equal"
    elif m["inequality"] < 60:
        interp["inequality"] = "Moderate inequality"
    else:
        interp["inequality"] = "Severe: risk of division"

    if m["sustainability"] > 70:
        interp["sustainability"] = "Plenty of ecological margin"
    elif m["sustainability"] > 40:
        interp["sustainability"] = "Warning signs"
    else:
        interp["sustainability"] = "Collapse imminent"

    return interp

def analyze_orientation(final):
    """Analyze dominant orientation based on final metrics"""
    scores = {
        "Efficiency-oriented": final["gdp"],
        "Happiness-oriented": final["happiness"],
        "Freedom-oriented": final["freedom"],
        "Equality-oriented": 100 - final["inequality"],
        "Sustainability-oriented": final["sustainability"]
    }
    dominant = max(scores, key=scores.get)
    return dominant, scores

def explain_final_metrics(final):
    """Print final metrics, ending, and orientation analysis"""
    interp = interpret_metrics(final)
    print("\n=== Final Metrics ===")
    for key in ["gdp", "happiness", "freedom", "inequality", "sustainability"]:
        val = final[key]
        print(bar_line(key.capitalize(), val, interp[key]))

    print("\n=== Ending ===")
    if final["happiness"] <= 0:
        print("💥 Society collapsed: Happiness reached 0.")
    elif final["gdp"] <= 0:
        print("📉 Society collapsed: GDP reached 0.")
    elif final["sustainability"] <= 0:
        print("🌍 Society collapsed: Sustainability reached 0.")
    elif final["freedom"] <= 0:
        print("🔒 Society collapsed: Freedom reached 0.")
    elif final["inequality"] >= 100:
        print("⚖️ Society collapsed: Inequality reached 100.")
    else:
        print("🎉 Your society successfully survived!")

    dominant, scores = analyze_orientation(final)
    print(f"\n=== Orientation Analysis ===")
    for k, v in scores.items():
        mark = "👑" if k == dominant else " "
        print(f"{mark} {k} ({ORIENTATION_MAP[k]}): {v}")
    print(f"\nYour society pursued '{dominant} ({ORIENTATION_MAP[dominant]})' the most.")
