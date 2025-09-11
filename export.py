"""
export.py
Exports the simulation state to JSON for Unity or external visualization.
"""

import json
import os
from datetime import datetime

def export_state(metrics, history, path="export/"):
    os.makedirs(path, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"state_{timestamp}.json"
    export_data = {
        "final_metrics": metrics.to_dict(),
        "history": history
    }
    with open(os.path.join(path, filename), "w", encoding="utf-8") as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    print(f"State exported to {os.path.join(path, filename)}")
