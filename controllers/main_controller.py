import asyncio
import time
import tkinter
from models import KartCombo
from services import *
from views import MainView


class MainController:
    def __init__(self, main_view: MainView):
        self.main_view = main_view
        self.combos: list[KartCombo] = []
        self.showing_combos: list[KartCombo] = []
        self.filter_dict: dict[str, tkinter.StringVar] = {}

        self.kart_attributes = [name for name, value in KartCombo.__dict__.items()
                                if isinstance(value, property)]
        self.kart_attribute_names = ["Name",
                                     "Ground Speed", "Water Speed",
                                     "Air Speed", "Anti-Gravity Speed",
                                     "Acceleration", "Weight",
                                     "Ground Handling", "Water Handling",
                                     "Air Handling", "Anti-Gravity Handling",
                                     "Traction", "Mini-Turbo", "Invincibility",
                                     "Inward drifting", "Vehicle Size"]

        self.create_filters()

        self.main_view.create_button("Filter", self.filter_list)
        self.main_view.create_button("Clear cache", delete_cache)

        asyncio.run(self.fetch_data())

    def create_filters(self):
        for attribute_name in self.kart_attribute_names:
            if (attribute_name == "Name"
                    or attribute_name == "Inward drifting"
                    or attribute_name == "Vehicle Size"):
                continue

            for min_or_max in ["Min. ", "Max. "]:
                self.add_filter(attribute_name, min_or_max)

    def add_filter(self, attribute_name, min_or_max):
        if min_or_max == "Min. ":
            value = "0"
            column = 0
        else:
            value = "20"
            column = 2

        name = min_or_max + attribute_name

        filter_var = tkinter.StringVar()
        filter_var.set(value)
        self.filter_dict[name] = filter_var

        self.main_view.create_filter(name,
                                     self.filter_dict[name],
                                     self.kart_attribute_names
                                     .index(attribute_name) - 1,
                                     column)

    def filter_list(self):
        new_combos: list[KartCombo] = []

        for combo in self.combos:
            if self.filter_combo(combo):
                new_combos.append(combo)

        print(f"Filtered {len(new_combos)} combos")

        self.showing_combos = new_combos

        self.main_view.update_table(self.showing_combos)

    def filter_combo(self, combo: KartCombo):
        for i in range(len(self.kart_attributes)):
            attribute = self.kart_attributes[i]
            attribute_name = self.kart_attribute_names[i]
            for min_or_max in ["Min. ", "Max. "]:
                try:
                    current_value = self.filter_dict[min_or_max +
                                                     attribute_name].get()
                except:
                    continue

                current_attribute = getattr(combo, attribute)

                if isinstance(current_attribute, int):
                    current_value = int(current_value)
                    if min_or_max == "Max. ":
                        if current_attribute > current_value:
                            return False
                    else:
                        if current_attribute < current_value:
                            return False

        return True

    async def fetch_data(self):
        load_start = time.perf_counter_ns()

        if cache_exists():
            try:
                print("Loading cache")
                self.combos = load_cache()
            except Exception as ex:
                print(f"Loading cache failed {ex}")
                delete_cache()
                await self.fetch_data()
                return
        else:
            print("Generating kart combos")
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

            save_cache(self.combos)

        self.showing_combos = self.combos

        load_end = time.perf_counter_ns()
        ms = (load_end - load_start) // 1000000

        print(f"Made {len(self.combos)} combos in {ms}ms")

        self.create_table()
        self.main_view.create_selected_labal()

    def create_table(self):
        self.main_view.create_table(
            self.kart_attributes,
            self.kart_attribute_names,
            self.showing_combos
        )
