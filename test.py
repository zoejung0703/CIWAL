"""
test.py
터미널에서 턴별 정책 선택 → 결과 출력 → state.json 저장
"""

import json
from simulation import load_policy_data, run_simulation
from export import export_state

def main():
    turns = load_policy_data()
    choices = {}

    print("=== 가치 선택 시뮬레이션 ===")
    for turn in turns:
        print(f"\n턴 {turn.turn_id}: {turn.era}")
        print(f"씬 구성: {turn.scene}")
        for i, p in enumerate(turn.policies):
            print(f"  [{i+1}] {p.name} ({p.philosopher}: \"{p.quote}\")")

        if not turn.policies:
            continue

        while True:
            try:
                choice = int(input("정책 선택: ")) - 1
                if 0 <= choice < len(turn.policies):
                    chosen = turn.policies[choice]
                    print(f"선택됨: {chosen.name}")
                    choices[turn.turn_id] = chosen.id
                    break
            except Exception:
                pass
            print("잘못된 입력입니다. 다시 입력하세요.")

    # 시뮬레이션 실행
    history = run_simulation(turns, choices)

    # 결과 출력
    print("\n=== 최종 결과 ===")
    for h in history:
        print(f"턴 {h['turn']} ({h['era']}) - 선택: {h['choice']}")
        print(f"  지표: {h['metrics']}")

    # state.json 저장
    with open("export/state.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    print("\n결과가 export/state.json에 저장되었습니다.")

if __name__ == "__main__":
    main()
