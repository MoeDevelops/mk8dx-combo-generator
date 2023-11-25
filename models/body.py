from models.terrain_stats import TerrainStats
from models.stats import Stats


class Body(Stats):
    is_inward_drift: bool

    def __init__(self, name: str, speed: TerrainStats, acceleration: int, weight: int, handling: TerrainStats, traction: int, mini_turbo: int, invincibility: int, is_inward_drift: bool):
        super().__init__(name, speed, acceleration, weight,
                         handling, traction, mini_turbo, invincibility)
        self.is_inward_drift = is_inward_drift
