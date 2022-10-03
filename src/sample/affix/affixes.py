from pathlib import Path
import json


class Affix:
    name = None
    tier = None
    _min = None
    _max = None
    avg = None

    def __init__(self, name, tier, _min, _max):
        self.name = name
        self.tier = tier
        self._min = 0.01 * _min
        self._max = 0.01 * _max
        self.avg = 0.01 * 0.5 * (_min + _max)

    def __str__(self):
        return "{}_T{:.0f}".format(self.name, self.tier)

    def from_dict(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)
        return self


DamageOverTimeT1 = Affix('DamageOverTime', 1, 10, 21)

FireDamageT1 = Affix('FireDamage', 1, 10, 21)
FireDamageT5 = Affix('FireDamage', 5, 75, 105)

SpellDamageT1 = Affix('SpellDamage', 1, 10, 21)

ElementalDamageT1 = Affix('ElementalDamage', 1, 9, 16)

ElementalDamageOverTimeT1 = Affix('ElementalDamageOverTime', 1, 18, 35)
ElementalDamageOverTimeT5 = Affix('ElementalDamageOverTime', 5, 124, 193)

CriticalStrikeChanceT1 = Affix('CriticalStrikeChance', 1, 26, 35)

SpellCriticalStrikeChanceT1 = Affix('SpellCriticalStrikeChance', 1, 35, 44)
SpellCriticalStrikeChanceT5 = Affix('SpellCriticalStrikeChance', 5, 96, 131)

CriticalStrikeMultiplierT1 = Affix('CriticalStrikeMultiplier', 1, 12, 16)
CriticalStrikeMultiplierT5 = Affix('CriticalStrikeMultiplier', 5, 37, 44)

CastSpeedT1 = Affix('CastSpeed', 1, 7, 9)
CastSpeedT5 = Affix('CastSpeed', 1, 21, 26)

ChanceToIgniteOnHitT1 = Affix('ChanceToIgniteOnHit', 1, 18, 21)
ChanceToIgniteOnHitT5 = Affix('ChanceToIgniteOnHit', 5, 42, 52)

affixes_dict = {'DamageOverTime': DamageOverTimeT1, 'FireDamage': FireDamageT1}

relpath = "../affix/affix_data.json"
filepath = Path(__file__).parent / relpath

file = open(filepath)
data = json.load(file)
file.close()

for item in data:
    a = Affix.from_dict(item)
    # print(a)
    affixes_dict[a['name']] = a


