#!/usr/bin/env python3
import numpy as np

f = open("ressources/day10.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Find the start
start = (0,0)
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            start = (i,j)

# Mapping between (from, pipe): to
mappingPipes = {
    ('|', (1, 0)): (1, 0),
    ('|', (-1, 0)): (-1, 0),
    ('-', (0, 1)): (0, 1),   
    ('-', (0, -1)): (0, -1), 
    ('L', (1, 0)): (0, 1),  
    ('L', (0, -1)): (-1, 0),  
    ('J', (1, 0)): (0, -1), 
    ('J', (0, 1)): (-1, 0), 
    ('7', (-1, 0)): (0, -1),  
    ('7', (0, 1)): (1, 0),  
    ('F', (-1, 0)): (0, 1), 
    ('F', (0, -1)): (1, 0)
}

# Find possible first motion
nbOfSteps = 1
firstPossibleMotion = [(1,0),(-1,0),(0,1),(0,-1)]
for motion in firstPossibleMotion:
    position = (start[0]+motion[0], start[1]+motion[1])
    char = lines[position[0]][position[1]]
    if (char, motion) in mappingPipes.keys():
        startMotion = (motion[0], motion[1])

# Make First Step
position = (start[0]+startMotion[0], start[1]+startMotion[1])
char = lines[position[0]][position[1]]
motion = mappingPipes[(char, startMotion)]

# Make the loop
visitedNodes = []
visitedNodes.append(position)
while True:
    position = (position[0]+motion[0], position[1]+motion[1])
    char = lines[position[0]][position[1]]
    visitedNodes.append(position)
    if char == "S":
        nbOfSteps += 1
        break
    motion = mappingPipes[(char, motion)]
    nbOfSteps += 1

print("Number of steps is: {}".format(nbOfSteps//2))

## Calculate the area using the trapezoid integral
prevNode = visitedNodes[0]
visitedNodes.append(prevNode)
area = 0
for node in visitedNodes[1:-1:]:
    area += (node[1]+prevNode[1])*(prevNode[0]-node[0])
    prevNode = (node[0], node[1])
    
area = area //2

# Inside is: (area - perimeter//2 + 1)
print("Number of enclosed cells is: {}".format(area - nbOfSteps//2 + 1))