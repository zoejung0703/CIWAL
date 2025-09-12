"""
simulation.py
Turn progression, policy application, warnings, and endings
"""

import json
from models import Metrics, Policy, Turn


def load_policy_data(path="data/policy_data.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    turns = []
    for t in data["turns"]:
        policies = [
            Policy(
                p["id"],
                p["name"],
                p["effects"],
                p["philosopher"],
                p["quote"],
            )
            for p in t["policies"]
        ]
        turns.append(Turn(t["turn_id"], t["era"], t["scene"], policies))
    return turns


def check_warnings(metrics):
    warnings = []
    if metrics.happiness < 20:
        warnings.append("⚠️ Happiness is critically low. Social unrest is rising.")
    if metrics.gdp < 40:
        warnings.append("⚠️ Economy is weakening. Production is faltering.")
    if metrics.sustainability < 20:
        warnings.append("⚠️ Environmental collapse is imminent.")
    if metrics.freedom < 20:
        warnings.append("⚠️ Freedom is severely restricted. Authoritarianism grows.")
    if metrics.equality < 30:
        warnings.append("⚠️ Equality is dangerously low. Society is fragmenting.")
    return warnings


def apply_population_growth(metrics):
    """Population growth depends on GDP, happiness, sustainability."""
    gdp_factor = (metrics.gdp - 50) / 500  
    happiness_factor = (metrics.happiness - 50) / 2500  
    sustainability_factor = (metrics.sustainability - 50) / 1000  

    growth_factor = 1.0 + gdp_factor + happiness_factor + sustainability_factor
    growth_factor = max(0.7, min(1.3, growth_factor))  

    metrics.population = int(metrics.population * growth_factor)


def run_simulation(turns, choices):
    metrics = Metrics(
        gdp=30,
        happiness=50,
        freedom=45,
        equality=75,
        sustainability=70,
        population=50
    )
    history = []

    for turn in turns:
        choice_id = choices.get(turn.turn_id)
        policy = next((p for p in turn.policies if p.id == choice_id), None)

        if policy:
            metrics.update(policy.effects)

        apply_population_growth(metrics)
        warnings = check_warnings(metrics)

        record = {
            "turn": turn.turn_id,
            "era": turn.era,
            "choice": policy.name if policy else None,
            "metrics": metrics.to_dict(),
            "warnings": warnings,
            "effects": policy.effects if policy else {}
        }

        # Ending conditions
        if metrics.happiness <= 0:
            record["ending"] = "💥 Social collapse (Happiness 0)"
            history.append(record)
            break
        if metrics.gdp <= 0:
            record["ending"] = "📉 Economic collapse (GDP 0)"
            history.append(record)
            break
        if metrics.sustainability <= 0:
            record["ending"] = "🌍 Environmental collapse (Sustainability 0)"
            history.append(record)
            break
        if metrics.freedom <= 0:
            record["ending"] = "🔒 Authoritarian regime (Freedom 0)"
            history.append(record)
            break
        if metrics.equality <= 0:
            record["ending"] = "⚖️ Extreme inequality → Social breakdown"
            history.append(record)
 