from collections import deque
class Schedule:
    def __init__(self):
        self.schedule = {
            #each is a list of Section objects
            'mon': [],
            'tue': [],
            'wed': [],
            'thu': [],
            'fri': []
        }

        # self.mon = []
        # self.tue = []
        # self.wed = []
        # self.thu = []
        # self.fri = []

        self.sectsToAdd = deque()

    '''
    Add a section to the current schedule. If there is a clash
    then remove the section(s) that is being clashed with, save it 
    in sectToAdd. 
    Arguments:
        section: The section to add
    Returns:
        True if there was a clash, False if there wasn't
    '''
    def addSection(self, section) -> bool:
        removed = False
        for day in section.days:
            added = False
            for i in range(len(self.schedule[day])):
                _, end = self.schedule[day][i].time
                if section.time[0] > end: continue

                while i < len(self.schedule[day]) and section.time[1] > self.schedule[day][i].time[0]: 
                    self.sectsToAdd.append(self.schedule[day][i])
                    self.schedule[day][i].removeTiming(self.schedule[day][i].time[0], self.schedule[day][i].time[1])
                    self.removeSection(self.schedule[day][i])
                    removed = True

                #add the section
                added = True
                self.schedule[day].insert(i, section)
                break

            if(not added):
                self.schedule[day].append(section)

        return removed

    '''
    Remove a section from the caller's schedule. It needs to 
    remove the section from each day it is on.
    '''    
    def removeSection(self, section):
        for day in section.days:
            self.schedule[day].remove(section)