#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
import copy

f = open("ressources/day22.txt", "r") #Open File
lines = f.readlines() #Separate in lines

bricks = {}
bricksQueue = []
for i, line in enumerate(lines):
    coordinates = line.replace("\n", "").replace("~", ",").split(",")
    xlow, ylow, zlow, xhigh, yhigh, zhigh = [int(x) for x in coordinates]
    bricks[i] = (xlow, ylow, zlow, xhigh, yhigh, zhigh)
    bricksQueue.append([zlow, i])

#Make Bricks Fall, and save which one is under which
fallenBricks = {}
graphBelow = defaultdict(list)
bricksQueue.sort()
bricksQueue.reverse()

while len(bricksQueue):
    zlow, i = bricksQueue.pop()
    zmin = 1
    xlow, ylow, zlow, xhigh, yhigh, zhigh =  bricks[i]
    for k in fallenBricks:
        brick = fallenBricks[k]
        if (xlow >= brick[0] and xlow <= brick[3]) or (xhigh >= brick[0] and xhigh <= brick[3]) or (xlow < brick[0] and xhigh > brick[3]):
            if (ylow >= brick[1] and ylow <= brick[4]) or (yhigh >= brick[1] and yhigh <= brick[4]) or (ylow < brick[1] and yhigh > brick[4]):
                graphBelow[i].append(k)
                zmin = max(zmin, brick[5]+1)
    fallenBricks[i] = (xlow, ylow, zmin, xhigh, yhigh, zmin+(zhigh-zlow))

#Look which one supports which; i.e is exactly below by one row in z
graphIsSupportedBy = defaultdict(list)
for i in graphBelow:
    for k in graphBelow[i]:
        if fallenBricks[i][2] == (fallenBricks[k][5]+1):
            graphIsSupportedBy[i].append(k)

#If a brick is supported by one brick only, this one cannot be disintegrated
cannotBeDisintegrated = set()
for i in graphIsSupportedBy:
    if len(graphIsSupportedBy[i])==1:
        cannotBeDisintegrated.add(graphIsSupportedBy[i][0])

NbCanBeDistingrated = len(fallenBricks) - len(cannotBeDisintegrated);
print("Nb of bricks that can be disintegrated is: {}".format(NbCanBeDistingrated))

graphSupports = defaultdict(list)
for i in graphIsSupportedBy:
    for k in graphIsSupportedBy[i]:
        graphSupports[k].append(i)

def falls(fallenBricks, graphSupports, graphIsSupportedBy):
    nbFallen = 0
    newFallenBricks = set()
    
    for i in fallenBricks:
        for k in graphSupports[i]:
            graphIsSupportedBy[k].remove(i)
            if len(graphIsSupportedBy[k]) == 0:
                newFallenBricks.add(k)
                nbFallen += 1
    if nbFallen == 0:
        return nbFallen
    
    nbFallen += falls(newFallenBricks, graphSupports, graphIsSupportedBy)
    return nbFallen

nbFalls = 0
for i in cannotBeDisintegrated:
    gSupports, gSupported = copy.deepcopy(graphSupports), copy.deepcopy(graphIsSupportedBy)
    nbFalls += falls([i], gSupports, gSupported)
    
print("Nb of falls is: {}".format(nbFalls))