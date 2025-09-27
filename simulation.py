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
            for p in t.get("policies", [])
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
    if metrics.equality < 30:
        warnings.append("⚠️ 평등이 심각히 무너져 사회가 분열 조짐을 보입니다.")
    return warnings


def check_ending(metrics):
    if metrics.happiness <= 0:
        return "💥 사회 붕괴 (행복 0)"
    if metrics.gdp <= 0:
        return "📉 경제 파산 (GDP 0)"
    if metrics.sustainability <= 0:
        return "🌍 환경 붕괴 (지속 0)"
    if metrics.freedom <= 0:
        return "🔒 독재 사회 (자유 0)"
    if metrics.equality <= 0:
        return "⚖️ 사회 분열 (평등 0)"
    return None


def run_simulation(turns, choices):
    metrics = Metrics(
        gdp=30,             # 초기 GDP 지수
        happiness=50,       # 초기 행복 지수
        freedom=45,         # 초기 자유 지수
        equality=25,        # 초기 평등 지수
        sustainability=70,  # 초기 지속가능성
        population=50       # 초기 인구
    )
    history = []

    for turn in turns:
        choice_id = choices.get(turn.turn_id)
        policy = next((p for p in turn.policies if p.id == choice_id), None)

        if policy:
            metrics.update(policy.effects)

        # 인구 성장 (간단 모델)
        metrics.population = int(metrics.population * 1.2)

        # 단계적 경고 체크
        warnings = check_warnings(metrics)

        record = {
            "turn": turn.turn_id,
            "era": turn.era,
            "choice": policy.name if policy else None,
            "metrics": metrics.to_dict(),
            "warnings": warnings,
            "effects": policy.effects if policy else {}
        }

        # 즉시 엔딩 조건 (단일 함수로 판정)
        ending = check_ending(metrics)
        if ending:
            record["ending"] = ending
            history.append(record)
            break

        history.append(record)

    return history
