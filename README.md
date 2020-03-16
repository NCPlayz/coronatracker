# coronatracker

This is a simple tracker for COVID19 which uses the data for https://bing.com/covid and wraps it into usable data for Python programs.

```py
>>> import coronatracker 
>>> ct = coronatracker.CoronaTracker() 
>>> ct.fetch_results()
>>> ct.get_country('United Kingdom')
Country(total_stats=TotalStats(confirmed=1551, deaths=53, recovered=19), id='unitedkingdom', last_updated=datetime.datetime(2020, 3, 16, 23, 0, 12, 91000), areas=[], name='United Kingdom', lat=53.943838, long=-2.550564)
```

## Requirements

- Requests

## Install

```sh
$ python -m pip install -U coronatracker
```

