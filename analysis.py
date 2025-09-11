"""
analysis.py
시뮬레이션 결과 분석 및 그래프 출력
"""

import matplotlib.pyplot as plt
import json


def plot_results(history):
    turns = [h["turn"] for h in history]
    gdp = [h["metrics"]["gdp"] for h in history]
    hap = [h["metrics"]["happiness"] for h in history]
    fre = [h["metrics"]["freedom"] for h in history]
    ineq = [h["metrics"]["inequality"] for h in history]
    sus = [h["metrics"]["sustainability"] for h in history]

    plt.figure(figsize=(10,6))
    plt.plot(turns, gdp, label="GDP")
    plt.plot(turns, hap, label="Happiness")
    plt.plot(turns, fre, label="Freedom")
    plt.plot(turns, ineq, label="Inequality")
    plt.plot(turns, sus, label="Sustainability")
    plt.legend()
    plt.xlabel("Turn")
    plt.ylabel("Value")
    plt.title("Simulation Result")
    plt.show()


if __name__ == "__main__":
    with open("export/state.json", encoding="utf-8") as f:
        history = json.load(f)
    plot_results(history)
