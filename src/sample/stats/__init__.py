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

    def __iter__(self):
        yield self._pid
        yield self._name


class ParamValue:
    def __init__(self, pid, name, value):
        self._pid = pid
        self._name = name
        self._value = value

    def __iter__(self):
        yield self._pid
        yield self._name
        yield self._value

    def __str__(self):
        return self._name

    @property
    def pid(self):
        return self._pid

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self._value = value


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


class Stats:
    _dict = {}

    @staticmethod
    def put(p):
        Stats._dict[p.pid] = p

    @staticmethod
    def get(pid):
        return Stats._dict[pid]

    @staticmethod
    def size():
        return len(Stats._dict)

    @staticmethod
    def dict():
        return Stats._dict

    @staticmethod
    def load(d):
        Stats._dict = d


data_dir = Path(__file__).parents[3] / 'data'
filename = "stats_dict.pickle"
filepath = data_dir / filename
print(filepath)

if not os.path.exists(filepath):
    Stats.put(p_IncreasedCastSpeed)
    Stats.put(p_IncreasedDamage)
    Stats.put(p_IncreasedSpellDamage)
    Stats.put(p_IncreasedElementalDamage)
    Stats.put(p_IncreasedElementalDamageOverTime)
    Stats.put(p_IncreasedFireDamage)
    Stats.put(p_IncreasedDamageOverTime)
    Stats.put(p_IncreasedIgniteChance)
    Stats.put(p_IncreasedIgniteDuration)
    Stats.put(p_IncreasedCritChance)
    Stats.put(p_IncreasedCritMultiplier)
    Stats.put(p_FirePenetration)
    Stats.put(p_TotalMoreDamage)

    f = open(filepath, "wb")
    pickle.dump(Stats.dict(), f)
    f.close()
else:
    f = open(filepath, "rb")
    data = pickle.load(f)
    Stats.load(data)
