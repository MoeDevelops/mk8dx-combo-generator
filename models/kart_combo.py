from models.driver import Driver
from models.body import Body
from models.stats import Stats
from models.terrain_stats import TerrainStats


class KartCombo:
    driver: Driver
    body: Body
    tires: Stats
    glider: Stats
    stats: Stats

    def __init__(self, driver: Driver, body: Body, tires: Stats, glider: Stats):
        self.driver = driver
        self.body = body
        self.tires = tires
        self.glider = glider
        self.stats = self.driver + self.body + self.tires + self.glider

    @property
    def name(self):
        return self.stats.name

    @property
    def ground_speed(self):
        return self.stats.speed.ground

    @property
    def water_speed(self):
        return self.stats.speed.water

    @property
    def air_speed(self):
        return self.stats.speed.air

    @property
    def anti_gravity_speed(self):
        return self.stats.speed.anti_gravity

    @property
    def acceleration(self):
        return self.stats.acceleration

    @property
    def weight(self):
        return self.stats.weight

    @property
    def ground_handling(self):
        return self.stats.handling.ground

    @property
    def water_handling(self):
        return self.stats.handling.water

    @property
    def air_handling(self):
        return self.stats.handling.air

    @property
    def anti_gravity_handling(self):
        return self.stats.handling.anti_gravity

    @property
    def traction(self):
        return self.stats.traction

    @property
    def mini_turbo(self):
        return self.stats.mini_turbo

    @property
    def invincibility(self):
        return self.stats.invincibility

    @property
    def is_inward_drift(self):
        return self.body.is_inward_drift

    @property
    def vehicle_size(self):
        return self.driver.vehicle_size

    def __str__(self):
        return f"{self.name};{self.ground_speed};{self.water_speed};{self.air_speed};{self.anti_gravity_speed};{self.acceleration};{self.weight};{self.ground_handling};{self.water_handling};{self.air_handling};{self.anti_gravity_handling};{self.traction};{self.mini_turbo};{self.invincibility};{self.is_inward_drift};{self.vehicle_size.value}"
