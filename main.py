from Section import Section
from Schedule import Schedule
from collections import deque

import copy

classes = ["CIS 1200 Lecture", "CIS 1200 Recitation", 
           "CIS 1600 Lecture", "CIS 1600 Recitation", 
           "MEAM 2020 Lecture", "MEAM 2020 Recitation", 
           "ECON 0100 Lecture", "ECON 0100 Recitation", 
           "WRIT 0740"]

#fetch data
times = []
duration = 1
days = []

schedule = Schedule()
sections = []
for c in classes:
    sect = Section(c, times, duration, days)
    sections.append(sect)

sections.sort(key=lambda sched: (len(sched.times), -duration))

for section in sections:
    queue = deque()
    temp = copy.deepcopy(schedule)

    





sect1 = Section("CIS 1200", [[10.5, 11.5], [12.5, 13.5]], 1, ['mon', 'wed'])
sect2 = Section("CIS 1600", [[8.5, 10], [12.5, 14]], 1, ['mon', 'wed'])
sect3 = Section("CIS 1700", [[8.5, 10], [10, 12.5]], 1, ['mon', 'wed'])

sched = Schedule()

sect1.time = sect1.timings[1]
sect3.time = sect3.timings[1]
sched.addSection(sect1)
sched.addSection(sect3)
sect2.time = sect2.timings[1]

sched.addSection(sect2)
print(sched.schedule['wed'][0].name)
print()
print(sched.sectsToAdd[0].name)
print(sched.sectsToAdd[1].name)
# print(sched.schedule['wed'][1].name)

