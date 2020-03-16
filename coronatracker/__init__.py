from collections import namedtuple
from datetime import datetime
import requests

TotalStats = namedtuple('TotalStats', 'confirmed deaths recovered')
Country = namedtuple('Country', 'total_stats id last_updated areas name lat long')
SubArea = namedtuple('SubArea', 'total_stats id last_updated areas name lat long')  # for US States etc

class CoronaTracker:
    def __init__(self):
        self.countries = []
        self.total_stats = None

        self._data = {}

    def fetch_results(self):
        r = requests.get('https://bing.com/covid/data')

        self._data = r.json()
        self.countries = self.generate_areas(self._data['areas'])

    def generate_areas(self, areas, *, cls=Country):
        ret = []

        for area in areas:
            sub_areas = []

            if len(area['areas']) > 0:
                sub_areas = self.generate_areas(area['areas'], cls=SubArea)

            last_updated = datetime.fromisoformat(area['lastUpdated'][:-1])

            ret.append(cls(TotalStats(area['totalConfirmed'], area['totalDeaths'], area['totalRecovered']), area['id'], 
                       last_updated, sub_areas, area['displayName'], area['lat'], area['long']))

        return ret

    def get_country(self, name):
        for c in self.countries:
            if c.name == name:
                return c
