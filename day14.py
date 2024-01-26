#!/usr/bin/env python3
from collections import defaultdict
import numpy as np
import re

f = open("ressources/day14.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Gather Data
rockMap = []
for line in lines:
    line = line.replace("\n", "")
    rockMap.append(line)

#Get transpose to do calculation per line and not per column
def transpose(x):
	return list(map(list, zip(*x)))
#Get flip for other directions
def flip(x):
    return [xi[::-1] for xi in x]

rockMap = transpose(rockMap)
sum = 0
nbRows = len(rockMap[-1])
for line in rockMap:
    line = ''.join(line)
    unmovableRocks = [-1] + [m.start() for m in re.finditer('#', line)] + [nbRows]
    rollingRocks = [m.start() for m in re.finditer('O', line)]
    for (i,j) in zip(unmovableRocks[0:-1], unmovableRocks[1:]):
        rollingInBetween = list(filter(lambda rock: rock > i and rock < j, rollingRocks))
        newRollingPositions = [i+k+1 for k in list(range(len(rollingInBetween)))]
        sum += nbRows*len(newRollingPositions) - np.sum(newRollingPositions)
        
print("Sum of Rolling Rocks is: {}".format(int(sum)))

#Create the new map after rolling
def roll(rockMap):
    newMap = []
    nbRows = len(rockMap[-1])
    for line in rockMap:
        line = ''.join(line)
        unmovableRocks = [-1] + [m.start() for m in re.finditer('#', line)] + [nbRows]
        rollingRocks = [m.start() for m in re.finditer('O', line)]
        newRollingRocks = []
        for (i,j) in zip(unmovableRocks[0:-1], unmovableRocks[1:]):
            rollingInBetween = list(filter(lambda rock: rock > i and rock < j, rollingRocks))
            newRollingPositions = [i+k+1 for k in list(range(len(rollingInBetween)))]
            newRollingRocks += newRollingPositions
        newLine = ['#' if k in unmovableRocks else 'O' if k in newRollingRocks else '.'  for k in list(range(nbRows))]
        newMap.append(newLine)
    return newMap

#Do rolling in any direction
def performRollingForAnyDirection(rockMap, direction):
    if direction == "north":
        rockMap = transpose(rockMap)
        rockMap = roll(rockMap)
        rockMap = transpose(rockMap)
        direction = "west"
        
    elif direction == "west":
        rockMap = roll(rockMap)
        direction = "south"
        
    elif direction == "south":
        rockMap = transpose(rockMap)
        rockMap = flip(rockMap)
        rockMap = roll(rockMap)
        rockMap = flip(rockMap)
        rockMap = transpose(rockMap)
        direction = "east"   
        
    elif direction == "east":
        rockMap = flip(rockMap)
        rockMap = roll(rockMap)
        rockMap = flip(rockMap)
        direction = "north"
        
    return rockMap, direction

#Get the score
def score(rockMap):
    rockMap = transpose(rockMap)
    sum = 0
    nbRows = len(rockMap[-1])
    for line in rockMap:
        line = ''.join(line)
        rollingRocks = [m.start() for m in re.finditer('O', line)]
        sum += nbRows*len(rollingRocks) - np.sum(rollingRocks)
    return sum


# Find a cycle
rockMap = []
for line in lines:
    line = line.replace("\n", "")
    rockMap.append(line)

direction = "north"
visitedMaps = defaultdict(list)

i = 0
scores = []
while True:
    for j in range(4):
        rockMap, direction = performRollingForAnyDirection(rockMap, direction)
    scores.append(score(rockMap))
    if str(rockMap) in visitedMaps.keys():
        i += 1
        break
    i += 1
    visitedMaps[str(rockMap)].append(i)   

# Find which score to use
firstOccurence = visitedMaps[str(rockMap)][0]
secondOccurence = i
cycleLength = secondOccurence - firstOccurence

totalRotations = firstOccurence + (1000000000-firstOccurence) % cycleLength -1

print("Sum of Rolling Rocks after cycles is: {}".format(scores[totalRotations]))