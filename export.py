"""
export.py
JSON export for Unity integration
"""

import json
from simulation import load_policy_data, run_simulation

def export_state(choices, out_path="export/state.json"):
    """
    Run a simulation with given choices and export the full history to JSON.
    choices: dict {turn_id: policy_id}
    out_path: output JSON file path
    """
    turns = load_policy_data()
    history = run_simulation(turns, choices)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    return history  # return for direct use in Unity


if __name__ == "__main__":
    # Example usage: Turn 1 = communal, Turn 2 = trade
    choices = {1: "communal", 2: "trade"}
    history = export_state(choices)
    print("✅ state.json exported with", len(history), "turns.")
