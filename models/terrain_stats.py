class TerrainStats:
    ground: int
    water: int
    air: int
    anti_gravity: int

    def __init__(self, ground: int, water: int, air: int, anti_gravity: int):
        self.ground = ground
        self.water = water
        self.air = air
        self.anti_gravity = anti_gravity
