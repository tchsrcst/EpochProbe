from pathlib import Path
import json


class Skill:
    name = None
    base_damage = None
    crit_chance = None
    crit_multiplier = None
    base_speed_per_sec = None
    ignite_chance = None
    added_damage_scaling = None
    damage_scaling_per_int_point = None

    def __init__(self, name, base_damage, crit_chance, crit_multiplier, base_speed_per_sec,
                 ignite_chance, added_damage_scaling, damage_scaling_per_int_point):
        self.name = name
        self.base_damage = base_damage
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier
        self.base_speed_per_sec = base_speed_per_sec
        self.ignite_chance = ignite_chance
        self.added_damage_scaling = added_damage_scaling
        self.damage_scaling_per_int_point = damage_scaling_per_int_point

    def from_dict(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)
        return self


TestSkill = Skill("TestSkill", 1.0, 0.05, 2.0, 1.0, 1.0, 1.0, 0.04)
Fireball = Skill("Fireball", 25.0, 0.05, 2.0, 1.467, 0.25, 1.25, 0.04)

skills_dict = {'TestSkill': TestSkill, 'Fireball': Fireball}

data_dir = Path(__file__).parents[3] / 'data'
filename = "skill_data.json"
filepath = data_dir / filename
print(filepath)

file = open(filepath)
data = json.load(file)
file.close()

for item in data:
    s = Skill.from_dict(item)
    # print(s)
    skills_dict[s['name']] = s

