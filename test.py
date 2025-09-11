import json
from simulation import load_policy_data, check_warnings
from models import Metrics
from analysis import explain_final_metrics, interpret_metrics, bar_line, LABELS

# ===== UI/입출력 관련 함수 =====
def display_turn_start(turn, metrics):
    print(f"\n=== 턴 {turn.turn_id} - {turn.era} ===")
    print("현재 지표 상태:")
    interp = interpret_metrics(metrics.to_dict())
    for key in ["gdp", "happiness", "freedom", "inequality", "sustainability"]:
        val = getattr(metrics, key)
        label = LABELS[key]
        print(bar_line(label, val, interp[label]))

    warnings = check_warnings(metrics)
    for w in warnings:
        print(w)

def display_policies(turn):
    print("\n정책 선택지:")
    for i, p in enumerate(turn.policies, 1):
        effs = ", ".join([f"{LABELS[k]}: {v:+d}" for k, v in p.effects.items()])
        print(f"{i}. {p.name} - {p.philosopher}: \"{p.quote}\" ({effs})")

def get_player_choice(turn):
    while True:
        try:
            choice = int(input("\n👉 선택할 정책 번호를 입력하세요: "))
            if 1 <= choice <= len(turn.policies):
                return turn.policies[choice - 1]
            else:
                print(f"1 ~ {len(turn.policies)} 사이 숫자 입력")
        except ValueError:
            print("숫자를 입력하세요.")

def display_final_result(final_metrics):
    explain_final_metrics(final_metrics)

# ===== 메인 게임 루프 =====
def main():
    turns = load_policy_data()

    metrics = Metrics(gdp=30, happiness=50, freedom=45,
                      inequality=25, sustainability=70, population=50)

    history = []
    for turn in turns:
        if not turn.policies:
            break

        display_turn_start(turn, metrics)
        display_policies(turn)
        policy = get_player_choice(turn)

        metrics.update(policy.effects)
        metrics.population = int(metrics.population * 1.2)

        history.append({
            "turn": turn.turn_id,
            "choice": policy.name,
            "metrics": metrics.to_dict(),
            "effects": policy.effects
        })

        print(f"\n✅ {policy.name} 선택됨!")

    final = history[-1]["metrics"]
    display_final_result(final)

if __name__ == "__main__":
    main()
