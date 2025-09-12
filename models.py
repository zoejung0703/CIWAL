"""
models.py
Core classes for simulation:
- Metrics: GDP, Happiness, Freedom, Equality, Sustainability, Population
- Policy: policy choice (effects, philosopher, quote)
- Turn: one era with available policies
"""

class Metrics:
    def __init__(self, gdp=50, happiness=50, freedom=50, equality=50, sustainability=50, population=100):
        self.gdp = gdp
        self.happiness = happiness
        self.freedom = freedom
        self.equality = equality
        self.sustainability = sustainability
        self.population = population

    def update(self, effects: dict):
        """Apply policy effects to metrics."""
        for key, value in effects.items():
            if hasattr(self, key):
                setattr(self, key, max(0, getattr(self, key) + value))  # prevent negatives

    def to_dict(self):
        return {
            "gdp": self.gdp,
            "happiness": self.happiness,
            "freedom": self.freedom,
            "equality": self.equality,
            "sustainability": self.sustainability,
            "population": self.population,
        }


class Policy:
    def __init__(self, policy_id, name, effects, philosopher, quote):
        self.id = policy_id
        self.name = name
        self.effects = effects
        self.philosopher = philosopher
        self.quote = quote

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "effects": self.effects,
            "philosopher": self.philosopher,
            "quote": self.quote
        }


class Turn:
    def __init__(self, turn_id, era, scene, policies):
        self.turn_id = turn_id
        self.era = era
        self.scene = scene
        self.policies = policies  # list of Policy

    def to_dict(self):
        return {
            "turn_id": self.turn_id,
            "era": self.era,
            "scene": self.scene,
            "policies": [p.to_dict() for p in self.policies]
        }
