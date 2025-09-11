"""
models.py
시뮬레이션에 필요한 기본 클래스 정의
- Metrics: GDP, 행복, 자유, 불평등, 지속, 인구
- Policy: 정책 선택지 (효과, 철학자, 문구)
- Turn: 특정 턴(시대), 선택 가능한 정책들
"""

class Metrics:
    def __init__(self, gdp=50, happiness=50, freedom=50, inequality=50, sustainability=50, population=100):
        self.gdp = gdp
        self.happiness = happiness
        self.freedom = freedom
        self.inequality = inequality
        self.sustainability = sustainability
        self.population = population

    def update(self, effects: dict):
        """정책 효과 적용"""
        for key, value in effects.items():
            if hasattr(self, key):
                setattr(self, key, max(0, getattr(self, key) + value))  # 음수 방지

    def to_dict(self):
        return {
            "gdp": self.gdp,
            "happiness": self.happiness,
            "freedom": self.freedom,
            "inequality": self.inequality,
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
