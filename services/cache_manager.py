import pickle
import os
from models.kart_combo import KartCombo

cache_path = "data/cache.pickle"


def cache_exists():
    return os.path.exists(cache_path)


def delete_cache():
    os.remove(cache_path)


def load_cache():
    with open(cache_path, "rb") as file:
        data: list[KartCombo] = pickle.load(file)
        return data


def save_cache(data: list[KartCombo]):
    with open(cache_path, "wb") as file:
        pickle.dump(data, file)
