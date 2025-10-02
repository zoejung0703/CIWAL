# export.py
import sys
import json
from simulation import load_policy_data, run_simulation

def export_state(choices, out_path="export/state.json"):
    turns = load_policy_data()
    history = run_simulation(turns, choices)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    return history

if __name__ == "__main__":
    # Unity will pass choices as JSON string arg
    if len(sys.argv) > 1:
        choices = json.loads(sys.argv[1])
    else:
        choices = {}
    history = export_state(choices)
    print(json.dumps(history, ensure_ascii=False))  # also print to stdout
