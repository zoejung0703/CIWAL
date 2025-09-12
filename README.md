# Societal Policy Simulation

An interactive text-based simulation/game that explores how different policy choices shape the development of societies over time.  
The system balances **five key metrics**:  
- **GDP** (economic productivity)  
- **Happiness** (well-being of citizens)  
- **Freedom** (political and personal liberty)  
- **Equality** (fairness and distribution of resources)  
- **Sustainability** (environmental and long-term balance)  

Population grows each turn, but its effect is indirect.  

---

## 🎮 Gameplay Flow
1. Each turn represents a historical era (Tribe → Ancient → Empire → Industrial → Modern → Future).  
2. You will be presented with **policy choices**.  
   - Each policy has **direct effects** on the metrics (e.g., GDP +6, Freedom -3).  
   - Philosophers or thinkers provide supporting quotes for context.  
3. After selecting a policy, the metrics update, and warnings appear if critical values drop too low.  
4. The simulation continues until:  
   - You reach the **Future Transition** (turn 12), or  
   - One metric collapses to 0 (Game Over).  

---

## ⚖️ Endings
The game can end in different ways:
- **Collapse by GDP** → Economic bankruptcy  
- **Collapse by Happiness** → Social unrest and breakdown  
- **Collapse by Freedom** → Authoritarian regime  
- **Collapse by Equality** → Severe inequality tears society apart  
- **Collapse by Sustainability** → Ecological collapse  

Or you reach **successful survival**, where a final report shows your society’s orientation.

---

## 📊 Analysis
At the end of the game, you will see:
- **Text-based bar charts** for each metric (0–100 scale, but can exceed 100 or fall below 0 for extremes).  
- A short description of the level (e.g., *“Strong economy”*, *“Authoritarian tendencies”*).  
- An **orientation analysis**:  
  - Efficiency-oriented (GDP)  
  - Well-being-oriented (Happiness)  
  - Freedom-oriented (Freedom)  
  - Equality-oriented (Equality)  
  - Sustainability-oriented (Sustainability)  

---

## 🛠️ Tech Stack
- **Python** for simulation logic and text interface  
- **Unity** (optional) for visualization (via JSON export)  
- **JSON data** for policies, eras, and philosophers  

---

## 🚀 Run the Game
1. Clone the repository  
2. Run the test driver:
   ```bash
   python test.py
