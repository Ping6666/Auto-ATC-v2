from typing import Dict, List

from core.storage.utils import load_airport_info

# --- #


class CoreDataStorage():

    # callsign -> callsign cols -> values
    storage: Dict[str, Dict[str, str | List]]

    def __init__(self):
        self.storage = {}
        return

    def append(self):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class DataStorage(CoreDataStorage):

    # rwy -> landing list -> id, start, end
    use_rwy_order: Dict[str, List[Dict[str, str | int | float]]]

    def __init__(self, icao: str):
        super().__init__()

        self.airport_info = load_airport_info(icao)

        _runways_order = self.airport_info['runways_order']
        self.use_rwy_order = {rwy: [] for rwy in _runways_order}
        return

    def _sample_multiple(self):
        raise NotImplementedError

    def sample_multiple(self):
        raise NotImplementedError
