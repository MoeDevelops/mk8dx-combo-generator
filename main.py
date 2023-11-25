from typing import List
from models.kart_combo import KartCombo
from services.part_converter import get_drivers, get_bodies, get_gliders, get_tires


drivers = get_drivers()
bodies = get_bodies()
gliders = get_gliders()
tires = get_tires()

combos: List[KartCombo] = []

print("Read files. Creating combos.")

for driver in drivers:
    for body in bodies:
        for tire in tires:
            for glider in gliders:
                combos.append(KartCombo(driver, body, tire, glider))

print(f"{len(combos)} combos created.")
