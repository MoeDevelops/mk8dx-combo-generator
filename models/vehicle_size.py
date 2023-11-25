from enum import Enum


class VehicleSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    def __str__(self):
        return self.value
