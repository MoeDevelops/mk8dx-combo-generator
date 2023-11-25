from vehicle_size import VehilceSize
from terrain_stats import TerrainStats
from stats import Stats


class Driver(Stats):
    vehicle_size: VehilceSize

    def __init__(self, speed: TerrainStats, acceleration: int, weight: int, handling: TerrainStats, traction: int, mini_turbo: int, invincibility: int, vehile_size: VehilceSize):
        super().__init__(speed, acceleration, weight,
                         handling, traction, mini_turbo, invincibility)
        self.vehicle_size = vehile_size
