"""
simulation.py
턴 진행 및 정책 적용 + 단계적 경고 + 즉시 엔딩 판정
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
        warnings.append("⚠️ 행복이 낮습니다. 사회 불안이 커지고 있습니다.")
    if metrics.gdp < 40:
        warnings.append("⚠️ 경제가 약화되고 있습니다.")
    if metrics.sustainability < 20:
        warnings.append("⚠️ 환경 파괴가 심각합니다.")
    if metrics.freedom < 20:
        warnings.append("⚠️ 자유가 크게 위축되었습니다.")
    if metrics.inequality > 70:
        warnings.append("⚠️ 불평등이 심각해 사회가 분열 조짐을 보입니다.")
    return warnings


def run_simulation(turns, choices):
    metrics = Metrics(
    gdp=30,             # 초기 GDP 지수
    happiness=50,       # 초기 행복 지수
    freedom=45,         # 초기 자유 지수
    inequality=25,      # 초기 불평등 지�