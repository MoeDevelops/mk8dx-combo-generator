from terrain_stats import TerrainStats


class Stats:
    speed: TerrainStats
    acceleration: int
    weight: int
    handling: TerrainStats
    traction: int
    mini_turbo: int
    invincibility: int

    def __init__(self, speed: TerrainStats, acceleration: int, weight: int, handling: TerrainStats, traction: int, mini_turbo: int, invincibility: int):
        self.speed = speed
        self.acceleration = acceleration
        self.weight = weight
        self.handling = handling
        self.traction = traction
        self.mini_turbo = mini_turbo
