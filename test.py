import sys
from simulation import load_policy_data, run_simulation


def display_metrics(metrics, previous=None):
    print("\n--- Current Metrics ---")
    for key, value in metrics.items():
        print(f"{key.capitalize()}: {value}")
    print("-----------------------")

def main():
    turns = load_policy_data()
    choices = {}
    history = []
    previous_metrics = None

    for turn in turns:
        print(f"\n=== Turn {turn.turn_id}: {turn.era} ===")
        print(f"Scene: {turn.scene}")

        if history:
            current_metrics = history[-1]["metrics"]
        else:
            current_metrics = {
                "gdp": 30,
                "happiness": 50,
                "freedom": 45,
                "equality": 75,
                "sustainability": 70,
                "population": 50
            }
        display_metrics(current_metrics, previous_metrics)

        print("Policy options:")
        for i, policy in enumerate(turn.policies, 1):
            print(f"{i}. {policy.name} ({policy.philosopher}: \"{policy.quote}\") "
                  f"Effects: {policy.effects}")

        choice = int(input(f"Select a policy (1-{len(turn.policies)}): "))
        chosen_policy = turn.policies[choice - 1]
        choices[turn.turn_id] = chosen_policy.id

        history = run_simulation(turns[:turn.turn_id], choices)
        previous_metrics = history[-1]["metrics"]

        if "ending" in history[-1]:
            print(f"\n*** GAME OVER: {history[-1]['ending']} ***")
            break

    print("\n=== Final Results ===")
    from analysis import final_report
    final_report(history)

if __name__ == "__main__":
    main()
