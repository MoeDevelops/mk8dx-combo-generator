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
        self.invincibility = invincibility

    def __add__(self, other):
        if isinstance(other, Stats) == False:
            raise ValueError("Unsupported operand type for +")

        other: Stats = other

        return Stats(self.name + ", " + other.name,
                     self.speed + other.speed,
                     self.acceleration + other.acceleration,
                     self.weight + other.weight,
                     self.handling + other.handling,
                     self.traction + other.traction,
                     self.mini_turbo + other.mini_turbo,
                     self.invincibility + other.invincibility)
