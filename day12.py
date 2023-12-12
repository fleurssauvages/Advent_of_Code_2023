#!/usr/bin/env python3
from collections import defaultdict
f = open("ressources/day12.txt", "r") #Open File
lines = f.readlines() #Separate in lines

visited = defaultdict(int)
def checkLine(spring, arrangement):
    key = spring + str(arrangement)
    if key in visited:
        return visited[key]
    if not spring:
        if len(arrangement) == 0:
            return 1
        else:
            return 0
    if spring[-1] == '?':
        visited[key] = checkLine(spring[:-1]+'#', arrangement)+checkLine(spring[:-1]+'.', arrangement)
        return visited[key]
    elif spring[-1] == '.':
        return checkLine(spring[:-1], arrangement)
    elif spring[-1] == '#':
        if len(arrangement) == 0:
            return 0
        if len(spring) < arrangement[-1]:
            return 0
        if "." in spring[-arrangement[-1]:]:
            return 0
        if spring[-arrangement[-1]-1] == '#':
            return 0
        visited[key] = checkLine(spring[:-arrangement[-1]-1], arrangement[:-1])
        return visited[key]

sumOfPossibilities = 0
sumOfExpandedPosibilities = 0
for line in lines:
    infos = line.split()
    
    spring = '.'+infos[0]
    arrangements = infos[1].split(',')
    arrangements = [int(x) for x in arrangements]
    sumOfPossibilities += checkLine(spring, arrangements)
    
    spring = spring+('?'+infos[0])*4
    arrangements = arrangements*5
    
    sumOfExpandedPosibilities += checkLine(spring, arrangements)
    
print("Sum of possibilities is: {}".format(sumOfPossibilities))
print("Sum of expanded possibilities is: {}".format(sumOfExpandedPosibilities))