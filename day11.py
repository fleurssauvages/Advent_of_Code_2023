#!/usr/bin/env python3
import numpy as np
from itertools import combinations

f = open("ressources/day11.txt", "r") #Open File
lines = f.readlines() #Separate in lines

space = []
for line in lines:
    line = line.replace("\n", "").replace(".", "0").replace("#", "1")
    space.append(list(line))

space = [map(int, line) for line in space]

emptyRows = [i for i, row in enumerate(space) if np.sum(row) == 0]
emptyColumns = [j for j, column in enumerate(zip(*space)) if np.sum(column) == 0]

galaxies = list(np.argwhere(np.array(space) == 1))

def inBetween(galaxy1, galaxy2, emptyRows, emptyColumns):
    nbRows = np.sum([min(galaxy1[0],galaxy2[0]) < row < max(galaxy1[0],galaxy2[0]) for row in emptyRows])
    nbColumns = np.sum([min(galaxy1[1],galaxy2[1]) < column < max(galaxy1[1],galaxy2[1]) for column in emptyColumns])
    return nbRows, nbColumns

def distance(galaxy1, galaxy2, emptyRows, emptyColumns, factor):
    nbRows, nbColumns = inBetween(galaxy1, galaxy2, emptyRows, emptyColumns)
    return abs(galaxy1[0] - galaxy2[0]) + nbRows*(factor-1) + abs(galaxy1[1] - galaxy2[1]) + nbColumns*(factor-1)

shortestPaths = [distance(galaxy1, galaxy2, emptyRows, emptyColumns, 2) for galaxy1, galaxy2 in combinations(galaxies, 2)]

print("Sum of paths is: {}".format(np.sum(shortestPaths)))

shortestPaths = [distance(galaxy1, galaxy2, emptyRows, emptyColumns, 1000000) for galaxy1, galaxy2 in combinations(galaxies, 2)]

print("Sum of expanded paths is: {}".format(np.sum(shortestPaths)))