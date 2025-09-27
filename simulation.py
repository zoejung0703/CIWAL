"""
simulation.py
Turn progression, policy effects, warnings, and ending checks
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
            for p in t.get("policies", [])
        ]
        turns.append(Turn(t["turn_id"], t["era"], t["scene"], policies))
    return turns


def check_warnings(metrics):
    warnings = []
    if metrics.happiness < 20:
        warnings.append("⚠️ Happiness is critically low. Social unrest is rising.")
    if metrics.gdp < 40:
        warnings.append("⚠️ The economy is weakening.")
    if metrics.sustainability < 20:
        warnings.append("⚠️ Environmental destruction is severe.")
    if metrics.freedom < 20:
        warnings.append("⚠️ Freedom is dangerously restricted.")
    if metrics.equality < 30:
        warnings.append("⚠️ Equality is dangerously low — society is fracturing.")
    return warnings


def check_ending(metrics):
    if metrics.happiness <= 0:
        return "💥 Collapse: Happiness reached zero."
    if metrics.gdp <= 0:
        return "📉 Collapse: GDP fell to zero."
    if metrics.sustainability <= 0:
        return "🌍 Collapse: Environment destroyed."
    if metrics.freedom <= 0:
        return "🔒 Collapse: Freedom eliminated — dictatorship."
    if metrics.equality <= 0:
        return "⚖️ Collapse: Equality has completely broken down."
    return None


def run_simulation(turns, choices):
    metrics = Metrics(
        gdp=30,             # Initial GDP
        happiness=50,       # Initial happiness
        freedom=45,         # Initial freedom
        equality=25,        # Initial equality
        sustainability=70,  # Initial sustainability
        population=50       # Initial population
    )
    history = []

    for turn in turns:
        choice_id = choices.get(turn.turn_id)
        policy = next((p for p in turn.policies if p.id == choice_id), None)

        if policy:
            metrics.update(policy.effects)

        # Simple population growth model
        metrics.population = int(metrics.population * 1.2)

        # Warnings
        warnings = check_warnings(metrics)

        record = {
            "turn": turn.turn_id,
            "era": turn.era,
            "choice": policy.name if policy else None,
            "metrics": metrics.to_dict(),
            "warnings": warnings,
            "effects": policy.effects if policy else {}
        }

        # Ending check
        ending = check_ending(metrics)
        if ending:
            record["ending"] = ending
            history.append(record)
            break

        history.append(record)

    return history
