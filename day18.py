#!/usr/bin/env python3
from collections import defaultdict
import numpy as np
import re
import heapq as hp
import time

f = open("ressources/day18.txt", "r") #Open File
lines = f.readlines() #Separate in lines

diggedCells = []
currentPosition = [0,0]
diggedCells.append(currentPosition)
perimeter = 1

for line in lines:
    instructions = line.replace("\n", "").split(" ")
    direction = instructions[0]
    size = int(instructions[1])
    
    currentPosition[0] += -size*(direction == "U")+size*(direction == "D")
    currentPosition[1] += size*(direction == "R")-size*(direction == "L")
    
    newPosition = currentPosition[:]
    diggedCells.append(newPosition)
    perimeter += size

## Calculate the interior using the trapezoid integral
prevNode = diggedCells[0]
interior = 0
for node in diggedCells[1::]:
    interior += (node[1]+prevNode[1])*(node[0]-prevNode[0])
    prevNode = (node[0], node[1])
    
## Pick Theorem, like day 10 but inverted
area = interior //2 + perimeter//2 + 1

print("Digged Area is: {}".format(area))

diggedCells = []
currentPosition = [0,0]
diggedCells.append(currentPosition)
hexaToDirection = {'0':'R', '1':'D', '2':'L', '3':'U'}
perimeter = 1

for line in lines:
    instructions = line.replace("\n", "").split(" ")
    direction = hexaToDirection[instructions[2][-2]]
    size = int(instructions[2][2:-2:], base=16)
    
    currentPosition[0] += -size*(direction == "U")+size*(direction == "D")
    currentPosition[1] += size*(direction == "R")-size*(direction == "L")
    
    newPosition = currentPosition[:]
    diggedCells.append(newPosition)
    perimeter += size

## Calculate the interior using the trapezoid integral
prevNode = diggedCells[0]
interior = 0
for node in diggedCells[1::]:
    interior += (node[1]+prevNode[1])*(node[0]-prevNode[0])
    prevNode = (node[0], node[1])
    
## Pick Theorem, like day 10 but inverted
area = interior //2 + perimeter//2 + 1

print("Digged Area with Hexa is: {}".format(area))