from models.driver import Driver
from models.body import Body
from models.stats import Stats


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
