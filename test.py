import json
from simulation import load_policy_data, check_warnings, check_ending, init_metrics
from analysis import explain_final_metrics, interpret_metrics, bar_line, LABELS

# ===== UI / Display Functions =====
def display_turn_start(turn, metrics):
    print(f"\n=== Turn {turn.turn_id} - {turn.era} ===")
    print("Current Metrics:")
    interp = interpret_metrics(metrics.to_dict())
    for key in ["gdp", "happiness", "freedom", "equality", "sustainability"]:
        print(bar_line(LABELS[key], getattr(metrics, key), interp[key]))

    for w in check_warnings(metrics):
        print(w)

def display_policies(turn):
    print("\nPolicy Options:")
    for i, p in enumerate(turn.policies, 1):
        effs = ", ".join([f"{LABELS[k]}: {v:+d}" for k, v in p.effects.items()])
        print(f"{i}. {p.name} - {p.philosopher}: \"{p.quote}\" ({effs})")

def get_player_choice(turn):
    while True:
        try:
            choice = int(input("\n👉 Enter the number of the policy to choose: "))
            if 1 <= choice <= len(turn.policies):
                return turn.policies[choice - 1]
            else:
                print(f"Enter a number between 1 and {len(turn.policies)}.")
        except ValueError:
            print("Please enter a valid number.")

def display_final_result(final_metrics, orientation):
    explain_final_metrics(final_metrics, orientation)

# ===== Main Game Loop =====
def main():
    turns = load_policy_data()
    metrics = init_metrics()

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

        ending = check_ending(metrics)
        if ending:
            print("\n=== Immediate Ending ===")
            print(ending)

            # Orientation at collapse
            from analysis import analyze_orientation
            dominant, scores = analyze_orientation(metrics.to_dict())
            display_final_result(metrics.to_dict(), {"dominant": dominant, "scores": scores})
            return  # Game over

        print(f"\n✅ You chose: {policy.name}")

    final = history[-1]["metrics"]

    from analysis import analyze_orientation
    dominant, scores = analyze_orientation(final)
    display_final_result(final, {"dominant": dominant, "scores": scores})

if __name__ == "__main__":
    main()
