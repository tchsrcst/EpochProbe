from src.core.data import affixes as af


class Input:
    name = None

    # character stats
    inc_cast_speed = 0.0
    inc_damage = 0.16
    inc_spell_damage = 0.0
    inc_elemental_damage = 0.0
    inc_elemental_dot = 0.0
    inc_fire_damage = 0.0
    inc_dot = 0.0
    inc_ignite_chance = 0.0
    inc_ignite_duration = 0.0
    inc_crit_chance = 0.0
    inc_crit_multiplier = 0.0
    # TODO
    fire_penetration = 0.0
    total_more_damage = 0.0

    def __init__(self, name):
        self.name = name

    def text(self):
        _text = 'increased_cast_speed=' + "{:.3f}".format(self.inc_cast_speed) + '\n' + \
            'increased_damage=' + "{:.3f}".format(self.inc_damage) + '\n' + \
            'increased_spell_damage=' + "{:.3f}".format(self.inc_spell_damage) + '\n' + \
                'increased_elemental_damage=' + "{:.3f}".format(self.inc_elemental_damage) + '\n' + \
                'increased_elemental_dot=' + "{:.3f}".format(self.inc_elemental_dot) + '\n' + \
                'increased_fire_damage=' + "{:.3f}".format(self.inc_fire_damage) + '\n' + \
                'increased_dot=' + "{:.3f}".format(self.inc_dot) + '\n' + \
                'increased_ignite_chance=' + "{:.3f}".format(self.inc_ignite_chance) + '\n' + \
                'increased_ignite_duration=' + "{:.3f}".format(self.inc_ignite_duration) + '\n' + \
                'increased_crit_chance=' + "{:.3f}".format(self.inc_crit_chance) + '\n' + \
                'increased_crit_multiplier=' + "{:.3f}".format(self.inc_crit_multiplier)
                # TODO
                # 'fire_penetration=' + "{:.3f}".format(self.fire_penetration) + '\n' + \
                # 'total_more_damage=' + "{:.3f}".format(self.total_more_damage)
        return _text

    def print(self):
        print('-'*40)
        print('Input:', self.name)
        print('BASE')
        if self.inc_cast_speed != 0:
            print('increased_cast_speed =', "{:.2f}".format(self.inc_cast_speed))
        if self.inc_damage != 0:
            print('increased_damage =', "{:.2f}".format(self.inc_damage))
        if self.inc_spell_damage != 0:
            print('increased_spell_damage =', "{:.2f}".format(self.inc_spell_damage))
        if self.inc_elemental_damage != 0:
            print('increased_elemental_damage =', "{:.2f}".format(self.inc_elemental_damage))
        if self.inc_elemental_dot != 0:
            print('increased_elemental_dot =', "{:.2f}".format(self.inc_elemental_dot))
        if self.inc_fire_damage != 0:
            print('increased_fire_damage =', "{:.2f}".format(self.inc_fire_damage))
        if self.inc_dot != 0:
            print('increased_dot =', "{:.2f}".format(self.inc_dot))
        if self.inc_ignite_chance != 0:
            print('increased_ignite_chance =', "{:.2f}".format(self.inc_ignite_chance))
        if self.inc_ignite_duration != 0:
            print('increased_ignite_duration =', "{:.2f}".format(self.inc_ignite_duration))
        if self.inc_crit_chance != 0:
            print('increased_crit_chance =', "{:.2f}".format(self.inc_crit_chance))
        if self.inc_crit_multiplier != 0:
            print('increased_crit_multiplier =', "{:.2f}".format(self.inc_crit_multiplier))

        # TODO
        # if self.fire_penetration != 0:
        #     print('fire_penetration =', "{:.2f}".format(self.fire_penetration))
        # if self.total_more_damage != 0:
        #     print('total_more_damage =', "{:.2f}".format(self.total_more_damage))


InputBase = Input("Base")

InputElementalDot = Input("+ElementalDot_T1")
InputElementalDot.inc_elemental_dot += af.ElementalDamageOverTimeT1.avg

InputFireDamage = Input("+FireDamage_T1")
InputFireDamage.inc_fire_damage += af.FireDamageT1.avg

InputCastSpeed = Input("+CastSpeed_T1")
InputCastSpeed.inc_cast_speed += af.CastSpeedT1.avg

InputChanceToIgniteOnHit = Input("+ChanceToIgniteOnHit_T1")
InputChanceToIgniteOnHit.inc_ignite_chance += af.ChanceToIgniteOnHitT1.avg

InputSpellCriticalStrikeChance = Input("+SpellCriticalStrikeChance_T1")
InputSpellCriticalStrikeChance.inc_crit_chance += af.SpellCriticalStrikeChanceT1.avg

InputCriticalStrikeMultiplier = Input("+CriticalStrikeMultiplier_T1")
InputCriticalStrikeMultiplier.inc_crit_multiplier += af.CriticalStrikeMultiplierT1.avg
