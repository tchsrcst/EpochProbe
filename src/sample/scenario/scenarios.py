from pathlib import Path
import json


class Scenario:

    name = None
    increment = None
    ramp = None
    pause = None
    time = None

    def __init__(self, name, increment, ramp, pause):
        self.name = name
        self.increment = increment
        self.ramp = ramp
        self.pause = pause
        self.time = ramp + pause

    def from_dict(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)
        return self


BasicScenario = Scenario('BasicScenario', 1.0, 90.0, 10.0)
ShortScenario = Scenario('ShortScenario', 1.0, 10.0, 5.0)

scenarios_dict = {}

data_dir = Path(__file__).parents[3] / 'data'
filename = "scenario_data.json"
filepath = data_dir / filename
print(filepath)

file = open(filepath)
data = json.load(file)
file.close()

for item in data:
    s = Scenario.from_dict(item)
    # print(s)
    scenarios_dict[s['name']] = s
