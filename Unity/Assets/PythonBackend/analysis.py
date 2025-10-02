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
    """Return interpretation text for each metric"""
    return {
        "gdp": (
            "Top of the OECD, explosive growth" if m["gdp"] > 100 else
            "Advanced economy level" if m["gdp"] > 70 else
            "Developing economy" if m["gdp"] > 40 else
            "Underdeveloped, crisis level"
        ),
        "happiness": (
            "World-leading, like Northern Europe" if m["happiness"] > 70 else
            "Around the global average" if m["happiness"] > 50 else
            "Warning: rising social discontent" if m["happiness"] > 30 else
            "Collapse imminent, risk of rebellion"
        ),
        "freedom": (
            "Fully free society" if m["freedom"] > 70 else
            "Partially free" if m["freedom"] > 40 else
            "Authoritarian and repressive regime"
        ),
        "equality": (
            "Highly equal society" if m["equality"] > 70 else
            "Moderate equality" if m["equality"] > 40 else
            "Severe inequality, risk of division"
        ),
        "sustainability": (
            "Plenty of environmental capacity" if m["sustainability"] > 70 else
            "Warning signs emerging" if m["sustainability"] > 40 else
            "On the brink of collapse"
        ),
    }


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


def explain_final_metrics(final, orientation=None):
    interp = interpret_metrics(final)
    print("\n=== Final Metrics ===")
    for key in ["gdp", "happiness", "freedom", "equality", "sustainability"]:
        val = final[key]
        print(bar_line(LABELS[key], val, interp[key]))

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
    if orientation is None:
        dominant, scores = analyze_orientation(final)
        orientation = {"dominant": dominant, "scores": scores}

    print(f"\n=== Orientation Analysis ===")
    for k, v in orientation["scores"].items():
        mark = "👑" if k == orientation["dominant"] else " "
        print(f"{mark} {k} ({ORIENTATION_MAP[k]}): {v}")
    print(f"\nYour society most strongly pursued: '{orientation['dominant']} ({ORIENTATION_MAP[orientation['dominant']]})'.")
