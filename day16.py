#!/usr/bin/env python3
from collections import defaultdict
import numpy as np
import re

f = open("ressources/day16.txt", "r") #Open File
lines = f.readlines() #Separate in lines

mappingMirrors = {
    ('|', (0, 1)): [(1, 0), (-1, 0)],
    ('|', (0, -1)): [(1, 0), (-1, 0)],
    ('|', (1, 0)): [(1, 0)],
    ('|', (-1, 0)): [(-1, 0)],
    ('-', (0, 1)): [(0, 1)],
    ('-', (0, -1)): [(0, -1)],
    ('-', (1, 0)): [(0, 1), (0, -1)],
    ('-', (-1, 0)): [(0, 1), (0, -1)],
    ('/', (0, 1)): [(-1, 0)],
    ('/', (0, -1)): [(1, 0)],
    ('/', (1, 0)): [(0, -1)],
    ('/', (-1, 0)): [(0, 1)],
    ('\\', (1, 0)): [(0, 1)],
    ('\\', (-1, 0)): [(0, -1)],
    ('\\', (0, 1)): [(1, 0)],
    ('\\', (0, -1)): [(-1, 0)],
    ('.', (1, 0)): [(1, 0)],
    ('.', (-1, 0)): [(-1, 0)],
    ('.', (0, 1)): [(0, 1)],
    ('.', (0, -1)): [(0, -1)]
}

mirrorMap = []
for line in lines:
    mirrorLine = list(line.replace('\n', ''))
    mirrorMap.append(mirrorLine)
nbRows = len(mirrorMap)
nbCols = len(mirrorMap[0])

start = (0,0)
startingDirection = (0,1)
beams = [[start, startingDirection]]

def energizing(beams, mirrorMap):
    energized = defaultdict(list)
    energized[start].append(0)
    while len(beams)>0:
        beam = beams.pop()
        currentChar = mirrorMap[beam[0][0]][beam[0][1]]
        newDirections = mappingMirrors[(currentChar, beam[1])]
        for direction in newDirections:
            newPosition = (beam[0][0] + direction[0], beam[0][1] + direction[1])
            if newPosition[0] > -1 and newPosition[0] < nbRows:
                if newPosition[1] > -1 and newPosition[1] < nbCols:
                    if direction not in energized[newPosition]:
                        energized[newPosition].append(direction)
                        beams.append([newPosition, direction])
    return len(energized.keys())

energized = energizing(beams, mirrorMap)
print("Number of energized tiles is: {}".format(energized))

maxEnergized = 0
for i in range(nbRows):
    start = (i,0)
    startingDirection = (0,1)
    beams = [[start, startingDirection]]
    energized = energizing(beams, mirrorMap)
    if energized > maxEnergized:
        maxEnergized = energized
for i in range(nbRows):
    start = (i,nbCols-1)
    startingDirection = (0,-1)
    beams = [[start, startingDirection]]
    energized = energizing(beams, mirrorMap)
    if energized > maxEnergized:
        maxEnergized = energized
for j in range(nbCols):
    start = (0,j)
    startingDirection = (1,0)
    beams = [[start, startingDirection]]
    energized = energizing(beams, mirrorMap)
    if energized > maxEnergized:
        maxEnergized = energized
for j in range(nbCols):
    start = (nbRows-1, j)
    startingDirection = (-1,0)
    beams = [[start, startingDirection]]
    energized = energizing(beams, mirrorMap)
    if energized > maxEnergized:
        maxEnergized = energized
print("Number of maxEnergized tiles is: {}".format(maxEnergized))