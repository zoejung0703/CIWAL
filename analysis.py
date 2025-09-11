"""
analysis.py - 텍스트 기반 시각화 (엔딩 + 성향 분석 포함)
"""

LABELS = {
    "gdp": "GDP",
    "happiness": "행복",
    "freedom": "자유",
    "inequality": "불평등",
    "sustainability": "지속성",
    "population": "인구"
}

ORIENTATION_MAP = {
    "효율 지향": "공리주의",
    "행복 지향": "복지주의",
    "자유 지향": "자유주의",
    "평등 지향": "롤스주의",
    "지속 지향": "환경주의"
}

def bar_line(name, value, desc, width=30):
    filled = int((max(0, min(value, 100)) / 100) * width)
    bar = "█" * filled + " " * (width - filled)
    return f"{name:<6} '{value:>3}': 0 [{bar}] 100  ({desc})"

def interpret_metrics(m):
    interp = {}
    # GDP
    if m["gdp"] > 100:
        interp["GDP"] = "OECD 최상위, 초고도 성장"
    elif m["gdp"] > 70:
        interp["GDP"] = "선진국 평균 수준"
    elif m["gdp"] > 40:
        interp["GDP"] = "중진국 수준"
    else:
        interp["GDP"] = "저개발 수준, 위기"

    # Happiness
    if m["happiness"] > 70:
        interp["행복"] = "세계 최상위, 북유럽 수준"
    elif m["happiness"] > 50:
        interp["행복"] = "세계 평균 수준"
    elif m["happiness"] > 30:
        interp["행복"] = "위험: 사회 불만 증가"
    else:
        interp["행복"] = "붕괴 직전, 반란 위험"

    # Freedom
    if m["freedom"] > 70:
        interp["자유"] = "완전 자유 사회"
    elif m["freedom"] > 40:
        interp["자유"] = "부분적 자유"
    else:
        interp["자유"] = "권위주의, 억압 체제"

    # Inequality
    if m["inequality"] < 30:
        interp["불평등"] = "평등사회"
    elif m["inequality"] < 60:
        interp["불평등"] = "보통 수준"
    else:
        interp["불평등"] = "심각: 사회 분열 위험"

    # Sustainability
    if m["sustainability"] > 70:
        interp["지속성"] = "환경 여유 충분"
    elif m["sustainability"] > 40:
        interp["지속성"] = "위기 조짐"
    else:
        interp["지속성"] = "붕괴 임박"

    return interp


def analyze_orientation(final):
    """최종 지표를 기반으로 성향 분석"""
    scores = {
        "효율 지향": final["gdp"],
        "행복 지향": final["happiness"],
        "자유 지향": final["freedom"],
        "평등 지향": 100 - final["inequality"],
        "지속 지향": final["sustainability"]
    }
    dominant = max(scores, key=scores.get)
    return dominant, scores


def explain_final_metrics(final):
    interp = interpret_metrics(final)
    print("\n=== 최종 지표 ===")
    for key in ["gdp", "happiness", "freedom", "inequality", "sustainability"]:
        val = final[key]
        label = LABELS[key]
        print(bar_line(label, val, interp[label]))

    print("\n=== 엔딩 결과 ===")
    if final["happiness"] <= 0:
        print("💥 사회는 행복을 완전히 잃고 붕괴했습니다.")
    elif final["gdp"] <= 0:
        print("📉 경제가 파산하며 사회는 무너졌습니다.")
    elif final["sustainability"] <= 0:
        print("🌍 환경이 붕괴하여 사회가 지속 불가능해졌습니다.")
    elif final["freedom"] <= 0:
        print("🔒 자유가 사라져 독재 사회가 되었습니다.")
    elif final["inequality"] >= 100:
        print("⚖️ 불평등이 극에 달해 사회가 분열되었습니다.")
    else:
        print("🎉 당신의 사회는 성공적으로 생존했습니다!")

    # 성향 분석 추가
    dominant, scores = analyze_orientation(final)
    print(f"\n=== 성향 분석 ===")
    for k, v in scores.items():
        mark = "👑" if k == dominant else " "
        print(f"{mark} {k}({ORIENTATION_MAP[k]}): {v}")
    print(f"\n당신의 사회는 '{dominant}({ORIENTATION_MAP[dominant]})' 성향을 가장 강하게 추구했습니다.")
