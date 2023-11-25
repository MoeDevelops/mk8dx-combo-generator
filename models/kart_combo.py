from models.driver import Driver
from models.body import Body
from models.stats import Stats
from models.terrain_stats import TerrainStats


class KartCombo:
    driver: Driver
    body: Body
    tires: Stats
    glider: Stats

    def __init__(self, driver: Driver, body: Body, tires: Stats, glider: Stats):
        self.driver = driver
        self.body = body
        self.tires = tires
        self.glider = glider

    @property
    def stats(self):
        return self.driver + self.body + self.tires + self.glider

    @property
    def vehicle_size(self):
        return self.driver.vehicle_size

    @property
    def is_inward_drift(self):
        return self.body.is_inward_drift
