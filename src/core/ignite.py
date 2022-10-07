
base_duration_sec = 3
base_damage = 39
base_dps = base_damage / base_duration_sec


class IgniteStack:
    num = None
    time_applied = None
    duration = None
    expire = None

    def __init__(self, num, time, duration):
        self.num = num
        self.time_applied = time
        self.duration = duration
        self.expire = self.time_applied + self.duration

    def __str__(self):
        return "Ignite#{:.0f}".format(self.num)

    def duration_left(self, time):
        return self.expire - time

    def is_expiring(self, time, increment):
        if time + increment > self.expire:
            return True
        else:
            return False

    def is_expired(self, time):
        if time >= self.expire:
            return True
        else:
            return False


