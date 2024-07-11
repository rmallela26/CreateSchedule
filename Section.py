class Section:
    def __init__(self, name, timings, duration, days):
        self.name = name
        self.timesLeft = timings[:]
        self.timings = timings[:]
        self.duration = duration
        self.days = days #str array: 'mon', 'tue', ...
        self.time = [] #contains start and end time
                        #same start and end across all days 
                        #it applies to

    def removeTiming(self, start, end):
        self.timesLeft.remove([start, end])

    def resetTimings(self):
        self.timesLeft = self.timings[:]
