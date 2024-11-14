class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:

    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2

    def get_different_clock(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        if res <= 0:
            return "00: 00: 00"
        hours = res // 3600
        minutes = (res % 3600) // 60
        seconds = (res % 3600) % 60
        return f"{str(hours).zfill(2)}: {str(minutes).zfill(2)}: {str(seconds).zfill(2)}"

    def __str__(self):
        return self.get_different_clock()

    def __len__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        if res <= 0:
            return 0
        return self.clock1.get_time() - self.clock2.get_time()


dt = DeltaClock(Clock(12, 42, 22), Clock(12, 22, 22))
print(dt)
print(len(dt))
