#!/usr/bin/env python3
import numpy as np
import re
from collections import defaultdict 

f = open("ressources/day3.txt", "r") #Open File
lines = f.readlines() #Separate in lines
notsymbol = "0123456789."
nbLines = np.size(lines)

sum = 0
for i, line in enumerate(lines):
    for n in re.finditer(r'\d+', line):
        edges = {(row, column) for row in (i-1, i, i+1) for column in range(n.start()-1, n.end()+1)}
        for edge in edges:
            row = max(0, min(nbLines-1,edge[0]))
            column = max(0, min(nbLines-1,edge[1]))
            if lines[row][column] not in notsymbol:
                sum += int(n.group())

print("Engine sum is: {}".format(sum))

gears = defaultdict(list)
for i, line in enumerate(lines):
    for n in re.finditer(r'\d+', line):
        edges = {(row, column) for row in (i-1, i, i+1) for column in range(n.start()-1, n.end()+1)}
        for edge in edges:
            row = max(0, min(nbLines-1,edge[0]))
            column = max(0, min(nbLines-1,edge[1]))
            if lines[row][column] == '*':
                gears[(row,column)].append(int(n.group()))

gearsSum = 0
for value in gears.values():
    if len(value) == 2:
        gearsSum += np.prod(value)

print("Gears sum is: {}".format(gearsSum))