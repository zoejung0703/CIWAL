# Civilization & Values: Policy Simulation Game

This is a prototype interactive simulation/game designed to demonstrate how **policy choices reflect value orientations** and how those choices shape society over time.

---

## 🎯 Concept
- Each turn represents a historical stage (tribal → empire → industrial → modern).  
- The player, as the decision-maker, selects one policy per turn.  
- Policies are inspired by famous philosophers and economists (e.g., Plato, Cicero, Keynes, Rawls, Sen).  
- Each policy affects five key metrics:  
  - **GDP** (Efficiency)  
  - **Happiness** (Well-being)  
  - **Freedom** (Liberty)  
  - **Inequality** (Equality/Fairness, inverse)  
  - **Sustainability** (Environmental balance)  

At the end of the simulation, the game provides:  
- **Final metrics visualization**  
- **Ending summary** (collapse or survival)  
- **Orientation analysis**: Did your society prioritize efficiency, freedom, happiness, equality, or sustainability?

---

## 🛠 Tech Stack
- **Python 3.10+**: Core simulation and text-based prototype  
- **Unity (planned)**: Interactive exhibition frontend  
- **Data**: Policies and effects stored in `data/policy_data.json`  

---

## 🚀 How to Run
1. Clone this repository  
2. Install Python 3.10+  
3. Run the prototype in console:
   ```bash
   python test.py
