#!/usr/bin/env python3
import numpy as np
from collections import deque, defaultdict
import copy

f = open("ressources/day21.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Gather Data
garden = []
for line in lines:
    line = line.replace("\n", "")
    garden.append(line)
    
for i, row in enumerate(garden):
    for j, char in enumerate(row):
        if char == "S":
            start = (i,j)
            garden[i] = garden[i][:j] + "." + garden[i][j+1:]
            
def nbPoints(garden, nbSteps, start):
    dataPoints = set()
    dataPoints.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nbRows = len(garden)
    nbCols = len(garden[0])

    for _ in range(nbSteps):
        newDataPoints = set()
        for point in dataPoints:
            for direction in directions:
                newPoint = (point[0]+direction[0], point[1]+direction[1])
                if newPoint[0] > -1 and newPoint[1] > -1 and newPoint[0] < nbRows and newPoint[1] < nbCols:
                    if garden[newPoint[0]][newPoint[1]] == ".":
                        newDataPoints.add(newPoint)
        dataPoints = copy.deepcopy(newDataPoints)
    
    return len(dataPoints)
    
nbPossiblesPoints = nbPoints(garden, 64, start)
print("Nb of possible steps is: {}".format(nbPossiblesPoints))

def nbPoints(garden, nbSteps, start):
    dataPoints = set()
    dataPoints.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nbRows = len(garden)
    nbCols = len(garden[0])

    for _ in range(nbSteps):
        newDataPoints = set()
        for point in dataPoints:
            for direction in directions:
                newPoint = (point[0]+direction[0], point[1]+direction[1])
                if garden[newPoint[0]%nbRows][newPoint[1]%nbCols] == ".":
                    newDataPoints.add(newPoint)
        dataPoints = copy.deepcopy(newDataPoints)
    return len(dataPoints)

nbTotalSteps = 26501365
nbRows = len(garden)
nbRepetitions = nbTotalSteps // nbRows
nbStepsLeft = nbTotalSteps % nbRows

def extrapolateQuadratic(nbStepsLeft, nbRows, nbRepetitions):
    f0 = nbPoints(garden, nbStepsLeft, start)
    f1 = nbPoints(garden, nbRows+nbStepsLeft, start)
    f2 = nbPoints(garden, 2*nbRows+nbStepsLeft, start)
    
    b0 = f0
    b1 = f1-f0
    b2 = f2-f1
    return b0 + b1*nbRepetitions + (nbRepetitions*(nbRepetitions-1)//2)*(b2-b1)
    
nbTotalPoints = extrapolateQuadratic(nbStepsLeft, nbRows, nbRepetitions)

print("Nb of possible steps is: {}".format(nbTotalPoints))