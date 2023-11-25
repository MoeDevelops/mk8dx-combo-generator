from typing import List
from services.csv_reader import read_csv
from models.body import Body
from models.driver import Driver
from models.stats import Stats
from models.terrain_stats import TerrainStats
from models.vehicle_size import VehicleSize


def get_drivers(file_path: str = "data/drivers.csv") -> List[Driver]:
    all_driver_data = read_csv(file_path)

    drivers: List[Driver] = []

    for driver_data in all_driver_data:
        name = driver_data[0]
        ground_speed = int(driver_data[1])
        water_speed = int(driver_data[2])
        air_speed = int(driver_data[3])
        anti_gravity_speed = int(driver_data[4])
        acceleration = int(driver_data[5])
        weight = int(driver_data[6])
        ground_handling = int(driver_data[7])
        water_handling = int(driver_data[8])
        air_handling = int(driver_data[9])
        anti_gravity_handling = int(driver_data[10])
        traction = int(driver_data[11])
        mini_turbo = int(driver_data[12])
        invincibility = int(driver_data[13])
        vehicle_size = VehicleSize(driver_data[14])

        driver = Driver(name,
                        TerrainStats(ground_speed, water_speed,
                                     air_speed, anti_gravity_speed),
                        acceleration, weight,
                        TerrainStats(ground_handling, water_handling,
                                     air_handling, anti_gravity_handling),
                        traction, mini_turbo, invincibility, vehicle_size)

        drivers.append(driver)

    return drivers


def get_bodies(file_path: str = "data/bodies.csv") -> List[Body]:
    all_body_data = read_csv(file_path)

    bodies: List[Body] = []

    for body_data in all_body_data:
        name = body_data[0]
        ground_speed = int(body_data[1])
        water_speed = int(body_data[2])
        air_speed = int(body_data[3])
        anti_gravity_speed = int(body_data[4])
        acceleration = int(body_data[5])
        weight = int(body_data[6])
        ground_handling = int(body_data[7])
        water_handling = int(body_data[8])
        air_handling = int(body_data[9])
        anti_gravity_handling = int(body_data[10])
        traction = int(body_data[11])
        mini_turbo = int(body_data[12])
        invincibility = int(body_data[13])
        is_inside_drift = body_data[14] == "True"

        body = Body(name,
                    TerrainStats(ground_speed, water_speed,
                                 air_speed, anti_gravity_speed),
                    acceleration, weight,
                    TerrainStats(ground_handling, water_handling,
                                 air_handling, anti_gravity_handling),
                    traction, mini_turbo, invincibility, is_inside_drift)

        bodies.append(body)

    return bodies


def get_gliders(file_path: str = "data/gliders.csv") -> List[Stats]:
    all_glider_data = read_csv(file_path)

    gliders: List[Stats] = []

    for glider_data in all_glider_data:
        name = glider_data[0]
        ground_speed = int(glider_data[1])
        water_speed = int(glider_data[2])
        air_speed = int(glider_data[3])
        anti_gravity_speed = int(glider_data[4])
        acceleration = int(glider_data[5])
        weight = int(glider_data[6])
        ground_handling = int(glider_data[7])
        water_handling = int(glider_data[8])
        air_handling = int(glider_data[9])
        anti_gravity_handling = int(glider_data[10])
        traction = int(glider_data[11])
        mini_turbo = int(glider_data[12])
        invincibility = int(glider_data[13])

        glider = Stats(name,
                       TerrainStats(ground_speed, water_speed,
                                    air_speed, anti_gravity_speed),
                       acceleration, weight,
                       TerrainStats(ground_handling, water_handling,
                                    air_handling, anti_gravity_handling),
                       traction, mini_turbo, invincibility)

        gliders.append(glider)

    return gliders


def get_tires(file_path: str = "data/tires.csv") -> List[Stats]:
    all_tire_data = read_csv(file_path)

    tires: List[Stats] = []

    for tire_data in all_tire_data:
        name = tire_data[0]
        ground_speed = int(tire_data[1])
        water_speed = int(tire_data[2])
        air_speed = int(tire_data[3])
        anti_gravity_speed = int(tire_data[4])
        acceleration = int(tire_data[5])
        weight = int(tire_data[6])
        ground_handling = int(tire_data[7])
        water_handling = int(tire_data[8])
        air_handling = int(tire_data[9])
        anti_gravity_handling = int(tire_data[10])
        traction = int(tire_data[11])
        mini_turbo = int(tire_data[12])
        invincibility = int(tire_data[13])

        tire = Stats(name,
                     TerrainStats(ground_speed, water_speed,
                                  air_speed, anti_gravity_speed),
                     acceleration, weight,
                     TerrainStats(ground_handling, water_handling,
                                  air_handling, anti_gravity_handling),
                     traction, mini_turbo, invincibility)

        tires.append(tire)

    return tires
