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

    def removeTiming(self, start, end):
        self.timesLeft.remove([start, end])

    def resetTimings(self):
        self.timesLeft = self.timings[:]

    def __str__(self):
        print("[" + self.name + "]: " + self.time)
