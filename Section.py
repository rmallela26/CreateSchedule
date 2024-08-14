class Section:
    def __init__(self, name, timings, duration):
        #All times represented as military time with decimals.
        #eg 2:15 is 14.25
        self.name = name
        self.timesLeft = timings[:]
        self.timings = timings[:]
        self.duration = duration
        # self.days = days #str array: 'mon', 'tue', ...
        self.time = [] #contains start and end time
                        #and days 

                        #format: [start, end, ['mon', 'wed']]

    def removeTiming(self, time):
        if time in self.timesLeft: self.timesLeft.remove(time)

    def resetTimings(self):
        self.timesLeft = self.timings[:]

    def __str__(self):
        return (f"[{self.name}]: {self.time}")
