#!/usr/bin/env python3
from collections import defaultdict

f = open("ressources/day12.txt", "r") #Open File
lines = f.readlines() #Separate in lines

visited = defaultdict(int)
def checkLine(spring, arrangement):
    key = spring + str(arrangement)
    if key in visited: # path has already been visited so we just use the stored value 
        return visited[key]
    if not spring: 
        if len(arrangement) == 0: # spring is empty and arrangement is empty too ! youhou ! 
            return 1
        else: # spring is empty but arrangement is not empty ! bouhou...
            return 0 
    if spring[-1] == '?': # we check both possibilites of the ?
        visited[key] = checkLine(spring[:-1]+'#', arrangement)+checkLine(spring[:-1]+'.', arrangement)
        return visited[key]
    elif spring[-1] == '.':
        return checkLine(spring[:-1], arrangement) # if there is a . we skip
    elif spring[-1] == '#':
        if len(arrangement) == 0: # # are left in the spring, but the arrangement is empty
            return 0
        if len(spring) < arrangement[-1]: # # spring number is shorter than the left arrangement
            return 0
        if "." in spring[-arrangement[-1]:]: # # possible spring pattern is shorter than the arrangement
            return 0
        if spring[-arrangement[-1]-1] == '#': # the spring possible pattern of # is longer than the arrangement
            return 0
        visited[key] = checkLine(spring[:-arrangement[-1]-1], arrangement[:-1]) # pattern is finally possible ! we remove it from spring and arragements tab
        return visited[key]

# Main Both Q1 and Q2
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