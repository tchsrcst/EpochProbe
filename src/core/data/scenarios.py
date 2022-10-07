

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

    def __str__(self):
        return self.name


BasicScenario = Scenario('BasicScenario', 1.0, 90.0, 10.0)
ShortScenario = Scenario('ShortScenario', 1.0, 10.0, 5.0)

scenarios_dict = [
    BasicScenario, ShortScenario
]
