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

    def __add__(self, other):
        if isinstance(other, TerrainStats) == False:
            raise ValueError("Unsupported operand type for +")

        other: TerrainStats = other

        return TerrainStats(self.ground + other.ground,
                            self.water + other.water,
                            self.air + other.air,
                            self.anti_gravity + other.anti_gravity)
