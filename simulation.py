"""
simulation.py
Turn progression, policy application, stepwise warnings, and immediate ending checks
"""

import json
from models import Metrics, Policy, Turn

def load_policy_data(path="data/policy_data.json"):
    """Load policies from JSON into Turn and Policy objects"""
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
    """Return warnings if metrics fall below critical thresholds"""
    warnings = []
    if metrics.happiness < 20:
        warnings.append("⚠️ Low happiness: risk of social unrest.")
    if metrics.gdp < 40:
        warnings.append("⚠️ Weak economy: GDP falling.")
    if metrics.sustainability < 20:
        warnings.append("⚠️ Environmental collapse is imminent.")
    if metrics.freedom < 20:
        warnings.append("⚠️ Freedom is severely restricted.")
    if metrics.inequality > 70:
        warnings.append("⚠️ High inequality: risk of division.")
    return warnings

def run_simulation(turns, choices):
    """Run the simulation based on given turns and chosen policies"""
    metrics = Metrics(
        gdp=30,            # initial GDP index
        happiness=50,      # initial happiness
        freedom=45,        # initial freedom
        inequality=25,     # initial inequality
        sustainability=70, # initial sustainability
        population=50      # initial population
    )
    history = []

    for turn in turns:
        choice_id = choices.get(turn.turn_id)
        policy = next((p for p in turn.policies if p.id == choice_id), None)

        if policy:
            metrics.update(policy.effects)

        # population growth (simple model)
        metrics.population = int(metrics.population * 1.2)

        # warnings
        warnings = check_warnings(metrics)

        record = {
            "turn": turn.turn_id,
            "era": turn.era,
            "choice": policy.name if policy else None,
            "metrics": metrics.to_dict(),
            "warnings": warnings,
            "effects": policy.effects if policy else {}
        }

        # immediate ending conditions
        if metrics.happiness <= 0:
            record["ending"] = "💥 Collapse: Happiness reached 0"
            history.append(record)
            break
        if metrics.gdp <= 0:
            record["ending"] = "📉 Collapse: GDP reached 0"
            history.append(record)
            break
        if metrics.sustainability <= 0:
            record["ending"] = "🌍 Collapse: Sustainability reached 0"
            history.append(record)
            break
        if metrics.freedom <= 0:
            record["ending"] = "🔒 Collapse: Freedom reached 0"
            history.append(record)
            break
        if metrics.inequality >= 100:
            record["ending"] = "⚖️ Collapse: Inequality reached 100"
            history.append(record)
            break

        history.append(record)

    return history
