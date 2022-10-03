import random

import numpy as np
import ignite


class Calculator:
    name = None
    input = None
    skill = None
    scenario = None
    x = None
    y = None

    """
        'inc' - increased
        'eff' - effective
        'dot' - damage over time
    """
    total_hit_inc_damage = None
    total_dot_inc_damage = None
    regular_hit_damage = None
    eff_crit_chance = None
    eff_crit_multiplier = None
    eff_crit_modifier = None
    crit_hit_damage = None
    eff_hit_damage = None
    eff_ignite_chance = None
    eff_ignite_duration = None
    eff_ignite_damage = None
    eff_ignite_dps_per_stack = None
    eff_cast_speed = None
    hits_per_second = None
    ignites_per_sec = None
    eff_hit_dps = None
    eff_ignite_dps = None
    eff_combined_dps = None

    def __init__(self, skill, _input, scenario):
        self.skill = skill
        self.input = _input
        self.scenario = scenario
        self.name = self.input.name

        self.total_hit_inc_damage = self.input.inc_damage + self.input.inc_elemental_damage \
                                    + self.input.inc_fire_damage + self.input.inc_spell_damage

        self.total_dot_inc_damage = self.input.inc_damage + self.input.inc_elemental_damage \
                                    + self.input.inc_fire_damage + self.input.inc_dot

        self.eff_ignite_chance = self.skill.ignite_chance + self.input.inc_ignite_chance
        self.eff_ignite_duration = ignite.base_duration_sec * (1.0 + self.input.inc_ignite_duration)
        self.eff_cast_speed = self.skill.base_speed_per_sec * (1.0 + self.input.inc_cast_speed)

        self.eff_ignite_damage = (1.0 + self.total_dot_inc_damage) * \
                                 (1.0 + self.input.inc_ignite_duration) * ignite.base_damage

        self.eff_ignite_dps_per_stack = (1.0 + self.total_dot_inc_damage) * ignite.base_dps

        self.eff_crit_chance = self.skill.crit_chance * (1.0 + self.input.inc_crit_chance)
        self.eff_crit_multiplier = self.skill.crit_multiplier + self.input.inc_crit_multiplier

        self.eff_crit_modifier = (1.0 - self.eff_crit_chance) + self.eff_crit_chance * self.eff_crit_multiplier

        self.regular_hit_damage = (1.0 + self.total_hit_inc_damage) * self.skill.base_damage
        self.crit_hit_damage = self.eff_crit_multiplier * self.regular_hit_damage
        self.eff_hit_damage = self.eff_crit_modifier * self.regular_hit_damage
        self.hits_per_second = self.eff_cast_speed

        self.ignites_per_sec = self.eff_ignite_chance * self.hits_per_second

        self.eff_hit_dps = self.eff_hit_damage * self.hits_per_second
        self.eff_ignite_dps = self.eff_ignite_damage * self.ignites_per_sec

        self.eff_combined_dps = self.eff_hit_dps + self.eff_ignite_dps

    def print(self):
        print('total_hit_increased_damage =', "{:.2f}".format(self.total_hit_inc_damage))
        print('total_dot_increased_damage =', "{:.2f}".format(self.total_dot_inc_damage))
        print('regular_hit_damage =', "{:.2f}".format(self.regular_hit_damage))
        print('effective_crit_chance =', "{:.2f}".format(self.eff_crit_chance))
        print('effective_crit_multiplier =', "{:.2f}".format(self.eff_crit_multiplier))
        print('effective_crit_modifier =', "{:.2f}".format(self.eff_crit_modifier))
        print('crit_hit_damage =', "{:.2f}".format(self.crit_hit_damage))
        print('effective_hit_damage =', "{:.2f}".format(self.eff_hit_damage))
        print('effective_ignite_chance =', "{:.2f}".format(self.eff_ignite_chance))
        print('effective_ignite_duration =', "{:.2f}".format(self.eff_ignite_duration))
        print('effective_ignite_damage =', "{:.2f}".format(self.eff_ignite_damage))
        print('effective_ignite_tick_damage =', "{:.2f}".format(self.eff_ignite_dps_per_stack))
        print('effective_cast_speed =', "{:.3f}".format(self.eff_cast_speed))
        print('hits_per_second =', "{:.2f}".format(self.hits_per_second))
        print('ignites_per_second =', "{:.2f}".format(self.ignites_per_sec))
        print('effective_hit_dps =', "{:.2f}".format(self.eff_hit_dps))
        print('effective_ignite_dps =', "{:.2f}".format(self.eff_ignite_dps))
        print('effective_combined_dps =', "{:.2f}".format(self.eff_combined_dps))

    def compute(self, verbose):
        t = self.scenario.increment
        self.x = np.arange(t, self.scenario.time + t, t)
        self.y = [[] for i in range(12)]

        self.calculate(verbose)
        self.simulate(verbose)

    # ----- Simplified calculations -----
    def calculate(self, verbose):
        total_hits = 0.0
        total_ignites = 0.0

        simplified_total_hit_damage = 0.0
        simplified_total_ignite_damage = 0.0
        simplified_total_combined_damage = 0.0

        # buffers for storing non integer parts
        hits_buffer = 0.0

        if verbose:
            print('-' * 80)

        t = self.scenario.increment

        for time in self.x:
            hit_damage = 0.0
            ignite_damage = 0.0

            # apply new hits during ramp time
            if time <= self.scenario.ramp:
                total_hits += self.hits_per_second * t
                total_ignites += self.ignites_per_sec * t
                hit_damage = self.eff_hit_dps
                ignite_damage = self.eff_ignite_dps
                simplified_total_hit_damage += self.eff_hit_dps
                simplified_total_ignite_damage += self.eff_ignite_dps
                simplified_total_combined_damage = simplified_total_hit_damage + simplified_total_ignite_damage

            # even if there is no new hits
            simplified_dps = 0.0 if time == 0.0 else simplified_total_combined_damage / self.scenario.ramp

            if verbose:
                print('time={:.1f}: hits={:.0f} ignites={:.0f} hit_damage={:.0f} ignite_damage={:.0f}'
                      ' total_hit_damage={:.0f} total_ignite_damage={:.0f} total_combined_damage={:.0f}'
                      .format(time, total_hits, total_ignites, hit_damage, ignite_damage,
                              simplified_total_hit_damage, simplified_total_ignite_damage,
                              simplified_total_combined_damage))

            self.y[0].append(total_hits)
            self.y[1].append(total_ignites)
            self.y[2].append(simplified_total_hit_damage)
            self.y[3].append(simplified_total_ignite_damage)
            self.y[4].append(simplified_total_combined_damage)
            self.y[5].append(simplified_dps)

        if verbose:
            print('hit_dps={:.2f} ignite_dps={:.2f} combined_dps={:.2f}'.format(
                  simplified_total_hit_damage / self.scenario.ramp,
                  simplified_total_ignite_damage / self.scenario.ramp,
                  simplified_total_combined_damage / self.scenario.ramp))

    # ----- Simulation of chances -----
    def simulate(self, verbose):
        simulated_total_hit_damage = 0.0
        simulated_total_ignite_damage = 0.0

        # buffers for storing non integer parts
        hits_buffer = 0.0

        ignites_arr = []
        ignites_counter = 0
        crits_counter = 0

        if verbose:
            print('-' * 80)

        t = self.scenario.increment

        random.seed()

        # emulation
        for time in self.x:
            simulated_hit_damage = 0

            # apply new hits during ramp time
            if time <= self.scenario.ramp:
                # ----- Simulated calculations -----
                new_hits = 0
                new_ignites = 0

                hits_buffer += self.hits_per_second * t
                while hits_buffer >= 1.0:
                    crit = random.random() < self.eff_crit_chance
                    if crit:
                        crits_counter += 1
                        simulated_hit_damage = self.crit_hit_damage
                        if verbose:
                            print("time:{:.1f} critical hit, damage={:.2f}".format(time, simulated_hit_damage))
                    else:
                        simulated_hit_damage = self.regular_hit_damage
                        # if verbose:
                        #    print("time:{:.1f} regular hit, damage={:.2f}".format(time, simulated_hit_damage))

                    simulated_total_hit_damage += simulated_hit_damage
                    hits_buffer -= 1.0
                    new_hits += 1

                if self.eff_ignite_chance > 0.0:
                    ignite_chance = self.eff_ignite_chance
                    while ignite_chance >= 1.0:
                        ignite_chance -= 1.0
                        new_ignites += 1
                    ignite_proc = random.random() < ignite_chance
                    if ignite_proc:
                        new_ignites += 1

                for i in range(new_ignites):
                    s = ignite.IgniteStack(ignites_counter, time, self.eff_ignite_duration)
                    ignites_arr.append(s)
                    if verbose:
                        print("time:{:.1f} {} applied".format(time, s))
                    ignites_counter += 1

            # even if there is no new hits
            current_ignites = len(ignites_arr)
            # current_ignite_dps = current_ignites * self.eff_ignite_dps_per_stack
            simulated_ignite_damage = 0.0

            for s in ignites_arr:

                if s.is_expired(time):
                    ignites_arr.remove(s)
                    if verbose:
                        print("time:{:.1f} {} has expired".format(time, s))
                elif s.is_expiring(time, t):
                    # portion of tick damage
                    ff = s.duration_left(time) / t
                    simulated_ignite_damage = ff * self.eff_ignite_dps_per_stack
                    if verbose:
                        print("time:{:.1f} {} f={:.1f} damage={:.2f}".format(time, s, ff, simulated_ignite_damage))
                else:
                    # regular tick
                    simulated_ignite_damage = self.eff_ignite_dps_per_stack
                    if verbose:
                        print("time:{:.1f} {} f={:.1f} damage={:.2f}".format(time, s, 1.0, simulated_ignite_damage))

                simulated_total_ignite_damage += simulated_ignite_damage

            simulated_total_combined_damage = simulated_total_hit_damage + simulated_total_ignite_damage
            simulated_dps = simulated_ignite_damage + simulated_hit_damage

            self.y[6].append(current_ignites)
            self.y[7].append(crits_counter)
            self.y[8].append(simulated_total_hit_damage)
            self.y[9].append(simulated_total_ignite_damage)
            self.y[10].append(simulated_total_combined_damage)
            self.y[11].append(simulated_dps)

        if verbose:
            print('hit_dps={:.2f} ignite_dps={:.2f} combined_dps={:.2f}'.format(
                  simulated_total_hit_damage / self.scenario.ramp,
                  simulated_total_ignite_damage / self.scenario.ramp,
                  simulated_total_combined_damage / self.scenario.ramp))
