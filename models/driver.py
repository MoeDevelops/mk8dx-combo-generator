from models.vehicle_size import VehicleSize
from models.terrain_stats import TerrainStats
from models.stats import Stats


class Driver(Stats):
    vehicle_size: VehicleSize

    def __init__(self, name: str, speed: TerrainStats, acceleration: int, weight: int, handling: TerrainStats, traction: int, mini_turbo: int, invincibility: int, vehile_size: VehicleSize):
        super().__init__(name, speed, acceleration, weight,
                         handling, traction, mini_turbo, invincibility)
        self.vehicle_size = vehile_size
