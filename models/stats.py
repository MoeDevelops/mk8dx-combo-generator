from models.terrain_stats import TerrainStats


class Stats:
    name: str
    speed: TerrainStats
    acceleration: int
    weight: int
    handling: TerrainStats
    traction: int
    mini_turbo: int
    invincibility: int

    def __init__(self, name: str, speed: TerrainStats, acceleration: int, weight: int, handling: TerrainStats, traction: int, mini_turbo: int, invincibility: int):
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.weight = weight
        self.handling = handling
        self.traction = traction
        self.mini_turbo = mini_turbo
