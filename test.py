import json
from simulation import load_policy_data, check_warnings, check_ending
from models import Metrics
from analysis import explain_final_metrics, interpret_metrics, bar_line, LABELS

# ===== UI / Display Functions =====
def display_turn_start(turn, metrics):
    print(f"\n=== Turn {turn.turn_id} - {turn.era} ===")
    print("Current Metrics:")
    interp = interpret_metrics(metrics.to_dict())
    for key in ["gdp", "happiness", "freedom", "equality", "sustainability"]:
        val = getattr(metrics, key)
        label = LABELS[key]
        print(bar_line(label, val, interp[label]))

    warnings = check_warnings(metrics)
    for w in warnings:
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

def display_final_result(final_metrics):
    explain_final_metrics(final_metrics)

# ===== Main Game Loop =====
def main():
    turns = load_policy_data()

    metrics = Metrics(gdp=30, happiness=50, freedom=45,
                      equality=25, sustainability=70, population=50)

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

        # Immediate ending check
        ending = check_ending(metrics)
        if ending:
            print("\n=== Immediate Ending ===")
            print(ending)
            return  # Game over

        print(f"\n✅ You chose: {policy.name}")

    # If no ending triggered, show final result
    final = history[-1]["metrics"]
    display_final_result(final)

if __name__ == "__main__":
    main()
