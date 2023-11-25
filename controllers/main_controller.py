import asyncio
import inspect
from models.kart_combo import KartCombo
from services.part_converter import get_bodies, get_drivers, get_gliders, get_tires
from views.main_view import MainView


class MainController:
    def __init__(self, main_view: MainView):
        self.main_view = main_view
        self.combos: list[KartCombo] = []
        self.showing_combos: list[KartCombo] = []
        asyncio.run(self.fetch_data())

    async def fetch_data(self):
        drivers, bodies, tires, gliders = await asyncio.gather(
            asyncio.to_thread(get_drivers),
            asyncio.to_thread(get_bodies),
            asyncio.to_thread(get_tires),
            asyncio.to_thread(get_gliders)
        )

        self.combos = [
            KartCombo(driver, body, tire, glider)
            for driver in drivers
            for body in bodies
            for tire in tires
            for glider in gliders
        ]

        self.showing_combos = self.combos

        print(f"Made {len(self.combos)} combos")

        self.create_table()

    def create_table(self):
        self.main_view.create_table(
            [name for name in KartCombo.__dict__
             if isinstance(getattr(KartCombo, name), property)],
            ["Name",
             "Ground Speed", "Water Speed", "Air Speed", "Anti-Gravity Speed",
             "Acceleration", "Weight",
             "Ground Handling", "Water Handling", "Air Handling", "Anti-Gravity Handling",
             "Traction", "Mini-Turbo", "Invincibility", "Inward drifing", "Vehicle Size"],
            self.showing_combos
        )
