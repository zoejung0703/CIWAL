"""
analysis.py
Final reporting and bar graph visualization of metrics
"""

def display_bar(label, value, desc):
    bar_length = 20
    filled = int((value / 100) * bar_length)
    bar = "[" + "#" * filled + "-" * (bar_length - filled) + "]"
    return f"{label} {value:3d}: 0 {bar} 100 ({desc})"


def describe_level(metric, value):
    if metric == "gdp":
        if value < 30: return "low income economy"
        if value < 70: return "mid-level economy"
        return "prosperous economy"
    elif metric == "happiness":
        if value < 30: return "widespread despair"
        if value < 70: return "moderate satisfaction"
        return "high life satisfaction"
    elif metric == "freedom":
        if value < 30: return "authoritarian"
        if value < 70: return "partly free"
        return "free society"
    elif metric == "equality":
        if value < 30: return "extreme inequality"
        if value < 70: return "moderate equality"
        return "high equality"
    elif metric == "sustainability":
        if value < 30: return "environmental collapse"
        if value < 70: return "moderate sustainability"
        return "sustainable society"
    else:
        return "n/a"


def analyze_orientation(history):
    orientation_scores = {"GDP": 0, "Happiness": 0, "Freedom": 0, "Equality": 0, "Sustainability": 0}
    for record in history:
        for k, v in record["effects"].items():
            if k in orientation_scores:
                orientation_scores[k.capitalize()] += v

    top_metric = max(orientation_scores, key=orientation_scores.get)
    return f"Most oriented toward: {top_metric} (values-based orientation)"


def final_report(history):
    final_metrics = history[-1]["metrics"]

    print("\n===== FINAL RESULTS =====")
    for key, value in final_metrics.items():
        if key == "population":
            continue
        desc = describe_level(key, value)
        print(display_bar(key.capitalize(), value, desc))

    print(f"\nFinal Population: {final_metrics['population']}")
    print("\nOrientation Analysis:", analyze_orientation(history))

    if "ending" in history[-1]:
        print("\nGAME OVER:", history[-1]["ending"])
    else:
        print("\n🌟 Your society has successfully survived through the ages!")
