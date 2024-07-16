from Section import Section
from Schedule import Schedule
from collections import deque

import copy

classes = ["CIS 1200 Lecture", "CIS 1200 Recitation", 
           "CIS 1600 Lecture", "CIS 1600 Recitation", 
           "MEAM 2020 Lecture", "MEAM 2020 Recitation", 
           "ECON 0100 Lecture", "ECON 0100 Recitation", 
           "WRIT 0740"]

def main():

    times = []
    duration = 1
    days = []

    schedule = Schedule()
    sections = []

    for c in classes:
        #fetch data for each class

        #create the section
        sect = Section(c, times, duration, days)
        sections.append(sect)

    #sort by shortest time, and then longest length first
    sections.sort(key=lambda sched: (len(sched.times), -duration))

    for section in sections:
        queue = deque()
        populateSchedule(schedule, section, queue)

        
def populateSchedule(parentSchedule, section, queue):
    for time in section.timesLeft:
        sect = copy.deepcopy(section)
        sect.timesLeft = []
        sect.time = time

        currSched = copy.deepcopy(parentSchedule)
        if not currSched.addSection(section): 
            if len(currSched.sectsToAdd) == 0:
                return currSched
            else:


            parentSchedule = currSched
            queue = deque() #empty queue
            break
        else:
            queue.append(currSched)

    finalizeSection(queue)

def finalizeSection(queue):
    while queue:
        currSched = queue.popleft()
        
        for sect in currSched.sectsToAdd:
            if len(sect.timesLeft) == 0:
                #schedule not possible
                continue
            else:
                populateSchedule(currSched, sect, queue)


'''
You have 10 sections (10 classes to fit). For each section:
go through the times it has left. Create a deepcopy for each
time left. Set the time of the curr deepcopy to a time. Add
the section. If it is successful and there is nothing else to 
add for this schedule break and done. Otherwise add to queue
and correct sectsToAdd for the schedule. Do for all the times
in the section. 

If haven't already broke and done, go through the queue. For 
each element on the queue, pop and do same as above. 
The above function shouldn't call the queue function. It should
just add stuff to the queue. This queue below function just keeps
going while stuff are on the queue, or a call to above function
returns successfully that sectsToAdd was emptied completely.
In this case we are done for this section. Set the scheudle
to this schedule and done. 
'''


# sect1 = Section("CIS 1200", [[10.5, 11.5], [12.5, 13.5]], 1, ['mon', 'wed'])
# sect2 = Section("CIS 1600", [[8.5, 10], [12.5, 14]], 1, ['mon', 'wed'])
# sect3 = Section("CIS 1700", [[8.5, 10], [10, 12.5]], 1, ['mon', 'wed'])

# sched = Schedule()

# sect1.time = sect1.timings[1]
# sect3.time = sect3.timings[1]
# sched.addSection(sect1)
# sched.addSection(sect3)
# sect2.time = sect2.timings[1]

# sched.addSection(sect2)
# print(sched.schedule['wed'][0].name)
# print()
# print(sched.sectsToAdd[0].name)
# print(sched.sectsToAdd[1].name)
# # print(sched.schedule['wed'][1].name)

