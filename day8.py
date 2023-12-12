#!/usr/bin/env python3
import numpy as np
import re
from collections import defaultdict

f = open("ressources/day8.txt", "r") #Open File
lines = f.readlines() #Separate in lines

instructions = lines[0].replace("\n", "");
graph = defaultdict(list)
lengthInstruction = len(instructions)

for line in lines[2::]:
    line = re.sub(r'[^\w\s]', '', line)
    nodes = line.split()
    graph[nodes[0]] = [nodes[1], nodes[2]]

currentPosition = "AAA"
i = 0

while currentPosition != "ZZZ":
    currentInstruction = instructions[i % lengthInstruction]
    if currentInstruction == "L":
        currentPosition = graph[currentPosition][0]
    elif currentInstruction == "R":
        currentPosition = graph[currentPosition][1]
    i += 1    

print("Total number of steps is: {}".format(i))

#Q2
startPositions = []
for key in graph.keys():
    if key[-1] == 'A':
        startPositions.append(key)

timeToReach = []
for currentPosition in startPositions:
    i = 0
    while currentPosition[-1] != 'Z':
        currentInstruction = instructions[i % lengthInstruction]
        if currentInstruction == "L":
            currentPosition = graph[currentPosition][0]
        elif currentInstruction == "R":
            currentPosition = graph[currentPosition][1]
        i += 1
    timeToReach.append(i)

timeToReachAll = np.lcm.reduce(timeToReach)
print("Total number of ghost steps is: {}".format(timeToReachAll))  