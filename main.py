from Section import Section
from Schedule import Schedule
from collections import deque

import copy
import csv

classes = ["CIS 1200 Lecture", "CIS 1200 Recitation", 
           "CIS 1600 Lecture", "CIS 1600 Recitation",  
           "ECON 0100 Lecture", "ECON 0100 Recitation", 
           "MEAM 2020 Lecture", "MEAM 2020 Recitation",
           "WRIT 0740"]

def main():

    schedule = Schedule()
    sections = []

    with open('data.txt', 'r') as file:
        # data = csv.reader(file)
        content  = file.read().strip()
        data = content.split('|')
    
        for line in data:
            if line == "" or line == "\n": break
            line = eval(line)
            # print(line[0])

        # for i in range(len(classes)):
            #fetch data for each class
            name = line[0]
            duration = line[1]
            oldTimes = line[2]

            #get rid of duplicates
            times = []
            times.append(oldTimes[0])
            for i in range(1, len(oldTimes)):
                if oldTimes[i] == times[-1]: continue
                times.append(oldTimes[i])

            times = blockTimes(times, 10, 24, False, ['tue', 'thu'])
            sect = Section(name, times, duration)
            sections.append(sect)

    #sort by shortest time, and then longest length first
    sections.sort(key=lambda sect: (len(sect.timings), -duration))

    for section in sections:
        queue = deque()
        schedule = populateSchedule(schedule, section, queue)
        if queue: schedule = finalizeSection(queue)

        if schedule == None:
            print("Schedule is impossible to fit")
            print("Tried to fit " + str(sections))
            print("Failed at " + str(section))
            return
        else:
            #reset all timesLeft for courses in schedule
            schedule.resetAllTimings()

    schedule.printSchedule()

        
def populateSchedule(parentSchedule, section, queue) -> Schedule:
    #add schedules to the local queue. If we get to the end
    #add the stuff on the localQueue to queue. Otherwise if 
    #gets quit somewhere in the middle, then we don't add
    #anything that was on the localQueue to queue (because
    #the class was fit)
    localQueue = deque()
    for time in section.timesLeft:
        sect = copy.deepcopy(section)
        sect.timesLeft = []
        sect.time = time

        currSched = copy.deepcopy(parentSchedule)
        if not currSched.addSection(sect): 
            if len(currSched.sectsToAdd) == 0:
                return currSched
            else:
                queue.append(currSched)
                return None
        else:
            localQueue.append(currSched)

    for item in localQueue:
        queue.append(item)
    
    return None

def finalizeSection(queue) -> Schedule:
    while queue:
        currSched = queue.popleft()
        
        while currSched.sectsToAdd:
            sect = currSched.sectsToAdd.popleft()
            if len(sect.timesLeft) == 0:
                #this schedule not possible
                continue
            else:
                candidate = populateSchedule(currSched, sect, queue)
                if candidate: return candidate
    return None

'''
Remove certain times from the array of potential times 
we can put things. This is called if the user pre picks
some classes on their own, and then calls fit. It is also
so the user can say they don't want classes after or before
or during a certain time.
Arguments:
    times: The array of potential times
    startTime: The start of time range
    endTime: The end of time range
    internal: Boolean that determines whether the times between
            or outside internal,external are the ones to block
    days: Array of which days this applies to 
Returns:
    The new times array
'''
def blockTimes(times, startTime, endTime, internal, days) -> list:
    newTimes = []
    start, end = 0, 0
    if internal:
        start = endTime
        end = startTime
    else:
        start = startTime
        end = endTime

    #for values > start and < end, add to newTimes
    #(only applies to days in days)
    for time in times:
        #check if days apply
        if not any(element in days for element in time[2]):
            newTimes.append(time)
            continue

        if time[0] >= start and time[1] <= end:
            newTimes.append(time)

    return newTimes
        


main()

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

