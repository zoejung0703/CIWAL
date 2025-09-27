"""
analysis.py - Text-based visualization (Ending + Orientation Analysis)
"""

LABELS = {
    "gdp": "GDP",
    "happiness": "Happiness",
    "freedom": "Freedom",
    "equality": "Equality",
    "sustainability": "Sustainability",
    "population": "Population"
}

ORIENTATION_MAP = {
    "Efficiency-Oriented": "Utilitarianism",
    "Happiness-Oriented": "Welfarism",
    "Freedom-Oriented": "Liberalism",
    "Equality-Oriented": "Rawlsian Justice",
    "Sustainability-Oriented": "Environmentalism"
}

def bar_line(name, value, desc, width=30):
    filled = int((max(0, min(value, 100)) / 100) * width)
    bar = "█" * filled + " " * (width - filled)
    return f"{name:<12} {value:>3}: 0 [{bar}] 100  ({desc})"

def interpret_metrics(m):
    interp = {}
    # GDP
    if m["gdp"] > 100:
        interp["GDP"] = "Top of the OECD, explosive growth"
    elif m["gdp"] > 70:
        interp["GDP"] = "Advanced economy level"
    elif m["gdp"] > 40:
        interp["GDP"] = "Developing economy"
    else:
        interp["GDP"] = "Underdeveloped, crisis level"

    # Happiness
    if m["happiness"] > 70:
        interp["Happiness"] = "World-leading, like Northern Europe"
    elif m["happiness"] > 50:
        interp["Happiness"] = "Around the global average"
    elif m["happiness"] > 30:
        interp["Happiness"] = "Warning: rising social discontent"
    else:
        interp["Happiness"] = "Collapse imminent, risk of rebellion"

    # Freedom
    if m["freedom"] > 70:
        interp["Freedom"] = "Fully free society"
    elif m["freedom"] > 40:
        interp["Freedom"] = "Partially free"
    else:
        interp["Freedom"] = "Authoritarian and repressive regime"

    # Equality
    if m["equality"] > 70:
        interp["Equality"] = "Highly equal society"
    elif m["equality"] > 40:
        interp["Equality"] = "Moderate equality"
    else:
        interp["Equality"] = "Severe inequality, risk of division"

    # Sustainability
    if m["sustainability"] > 70:
        interp["Sustainability"] = "Plenty of environmental capacity"
    elif m["sustainability"] > 40:
        interp["Sustainability"] = "Warning signs emerging"
    else:
        interp["Sustainability"] = "On the brink of collapse"

    return interp


def analyze_orientation(final):
    """Analyze based on final metrics"""
    scores = {
        "Efficiency-Oriented": final["gdp"],
        "Happiness-Oriented": final["happiness"],
        "Freedom-Oriented": final["freedom"],
        "Equality-Oriented": final["equality"],
        "Sustainability-Oriented": final["sustainability"]
    }
    dominant = max(scores, key=scores.get)
    return dominant, scores


def explain_final_metrics(final):
    interp = interpret_metrics(final)
    print("\n=== Final Metrics ===")
    for key in ["gdp", "happiness", "freedom", "equality", "sustainability"]:
        val = final[key]
        label = LABELS[key]
        print(bar_line(label, val, interp[label]))

    print("\n=== Ending ===")
    if final["happiness"] <= 0:
        print("💥 Society has lost all happiness and collapsed.")
    elif final["gdp"] <= 0:
        print("📉 The economy has gone bankrupt, leading to collapse.")
    elif final["sustainability"] <= 0:
        print("🌍 The environment has collapsed, making survival impossible.")
    elif final["freedom"] <= 0:
        print("🔒 Freedom has vanished — dictatorship has taken over.")
    elif final["equality"] <= 0:
        print("⚖️ Equality has completely broken down — society fractured.")
    else:
        print("🎉 Your society has survived successfully!")

    # Orientation analysis
    dominant, scores = analyze_orientation(final)
    print(f"\n=== Orientation Analysis ===")
    for k, v in scores.items():
        mark = "👑" if k == dominant else " "
        print(f"{mark} {k} ({ORIENTATION_MAP[k]}): {v}")
    print(f"\nYour society most strongly pursued: '{dominant} ({ORIENTATION_MAP[dominant]})'.")
