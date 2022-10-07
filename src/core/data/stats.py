from pathlib import Path
import os
import pickle


class Param:
    def __init__(self, pid, name):
        self._pid = pid
        self._name = name

    def pid(self):
        return self._pid

    def name(self):
        return self._name

    def __str__(self):
        return self._name

    def __iter__(self):
        yield self._pid
        yield self._name


class ParamValue:
    def __init__(self, pid, name, value):
        self._pid = pid
        self._name = name
        self._value = value

    @staticmethod
    def build(param, value):
        return ParamValue(param.pid, param.name, value)

    def get(self):
        return [self._name, self._value]


p_IncreasedCastSpeed = Param(0, "Increased Cast Speed")
p_IncreasedDamage = Param(1, "Increased Damage")
p_IncreasedSpellDamage = Param(2, "Increased Spell Damage")
p_IncreasedElementalDamage = Param(3, "Increased Elemental Damage")
p_IncreasedElementalDamageOverTime = Param(4, "Increased Elemental Damage over Time")
p_IncreasedFireDamage = Param(5, "Increased Fire Damage")
p_IncreasedDamageOverTime = Param(6, "Increased Damage over Time")
p_IncreasedIgniteChance = Param(7, "Increased Ignite Chance")
p_IncreasedIgniteDuration = Param(8, "Increased Ignite Duration")
p_IncreasedCritChance = Param(9, "Increased Crit Chance")
p_IncreasedCritMultiplier = Param(10, "Increased Crit Multiplier")
p_FirePenetration = Param(11, "Fire Penetration")
p_TotalMoreDamage = Param(12, "Total More Damage")

stats = [
    p_IncreasedCastSpeed,
    p_IncreasedDamage,
    p_IncreasedSpellDamage,
    p_IncreasedElementalDamage,
    p_IncreasedElementalDamageOverTime,
    p_IncreasedFireDamage,
    p_IncreasedDamageOverTime,
    p_IncreasedIgniteChance,
    p_IncreasedIgniteDuration,
    p_IncreasedCritChance,
    p_IncreasedCritMultiplier,
    p_FirePenetration,
    p_TotalMoreDamage,
]

DEFAULT_VALUE = 0.0

values = [
    ParamValue.build(p_IncreasedCastSpeed, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedDamage, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedSpellDamage, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedElementalDamage, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedElementalDamageOverTime, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedFireDamage, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedDamageOverTime, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedIgniteChance, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedIgniteDuration, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedCritChance, DEFAULT_VALUE),
    ParamValue.build(p_IncreasedCritMultiplier, DEFAULT_VALUE),
    ParamValue.build(p_FirePenetration, DEFAULT_VALUE),
    ParamValue.build(p_TotalMoreDamage, DEFAULT_VALUE),
]

data_dir = Path(__file__).parents[3] / 'data'
filename = "stats.pickle"
filepath = data_dir / filename
print(filepath)

if not os.path.exists(filepath):
    f = open(filepath, "wb")
    pickle.dump(stats, f)
    f.close()
else:
    f = open(filepath, "rb")
    stats = pickle.load(f)
