"""
simulation.py
턴 진행 및 정책 적용 로직
"""

import json
from models import Metrics, Policy, Turn

# 데이터 로딩
def load_policy_data(path="data/policy_data.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    turns = []
    for t in data["turns"]:
        policies = [Policy(p["id"], p["name"], p["effects"], p["philosopher"], p["quote"]) for p in t["policies"]]
        turns.append(Turn(t["turn_id"], t["era"], t["scene"], policies))
    return turns


def run_simulation(turns, choices):
    """
    turns: Turn 리스트
    choices: {턴번호: 정책ID} dict
    """
    metrics = Metrics(gdp=10, happiness=45, freedom=50, inequality=20, sustainability=90, population=30)  # 초기값
    history = []

    for turn in turns:
        choice_id = choices.get(turn.turn_id)
        policy = next((p for p in turn.policies if p.id == choice_id), None)

        if policy:
            metrics.update(policy.effects)

        # 인구는 매턴 성장률 반영 (간단 모델)
        metrics.population = int(metrics.population * 1.2)

        history.append({
            "turn": turn.turn_id,
            "era": turn.era,
            "choice": policy.name if policy else None,
            "metrics": metrics.to_dict()
        })

    return history


if __name__ == "__main__":
    turns = load_policy_data()
    choices = {1: "communal", 2: "trade"}  # 예시 선택
    result = run_simulation(turns, choices)
    print(json.dumps(result, indent=2, ensure_ascii=False))
