#!/usr/bin/env python3
import numpy as np

f = open("ressources/day6.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
times = list(map(int, lines[0].split()[1::]))
distances = list(map(int, lines[1].split()[1::]))

ways = []
for time, distance in zip(times, distances):
    endDistance = np.multiply(list(range(0, time, 1)), list(range(time, 0, -1)))
    ways.append(np.sum(endDistance > distance))

print("Ways to beat all the records is: {}".format(np.prod(ways)))

#Q2
time = int(''.join(lines[0].split()[1::]))
distance = int(''.join(lines[1].split()[1::]))

#BruteForce
# endDistance = np.multiply(list(range(0, time, 1)), list(range(time, 0, -1)))
# nbWays = np.sum(endDistance > distance)

#SmoothForce by dicho
def dichoMin(time, distance, minTime, maxTime):
    while minTime < maxTime:
        middleTime = (minTime + maxTime) // 2
        if (time - middleTime) * middleTime > distance:
            minTime = minTime
            maxTime = middleTime
        else:
            minTime = middleTime + 1
            maxTime = maxTime
    return minTime

def dichoMax(time, distance, minTime, maxTime):
    while minTime < maxTime:
        middleTime = (minTime + maxTime) // 2
        if (time - middleTime) * middleTime > distance:
            minTime = middleTime + 1
            maxTime = maxTime
        else:
            minTime = minTime
            maxTime = middleTime
    return minTime

minTime = dichoMin(time, distance, 1, time//2+1)
maxTime = dichoMax(time, distance, time//2-1, time-1)

nbWays = maxTime - minTime;
print("Ways to beat the race is: {}".format(nbWays))