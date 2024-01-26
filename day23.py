#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
import copy
import sys

f = open("ressources/day23.txt", "r") #Open File
lines = f.readlines() #Separate in lines

forestMap = []
for line in lines:
    forestMap.append(line.replace("\n", ""))
    
nbRows = len(forestMap)
nbCols = len(forestMap[0])

start = (0, 1)

graph = defaultdict(list)
directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(nbRows):
    for j in range(nbCols):
        if forestMap[i][j]==".":
            for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                    if forestMap[i+direction[0]][j+direction[1]] in ".<>^v":
                        graph[(i,j)].append((i+direction[0], j+direction[1]))
        if forestMap[i][j] in "<":
            direction = (0, -1)
            if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                if forestMap[i+direction[0]][j+direction[1]] in ".<>^v":
                    graph[(i,j)].append((i+direction[0], j+direction[1]))
        if forestMap[i][j] in ">":
            direction = (0, 1)
            if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                if forestMap[i+direction[0]][j+direction[1]] in ".<>^v":
                    graph[(i,j)].append((i+direction[0], j+direction[1]))
        if forestMap[i][j] in "v":
            direction = (1, 0)
            if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                if forestMap[i+direction[0]][j+direction[1]] in ".<>^v":
                    graph[(i,j)].append((i+direction[0], j+direction[1]))
        if forestMap[i][j] in "^":
            direction = (-1, 0)
            if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                if forestMap[i+direction[0]][j+direction[1]] in ".<>^v":
                    graph[(i,j)].append((i+direction[0], j+direction[1]))

def DFS(G,v,seen=None,path=None):
    if seen is None: 
        seen = set()
    if path is None: 
        path = [v]

    seen.add(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, copy.copy(seen), t_path))
    return paths

sys.setrecursionlimit(nbRows*nbCols)
paths = DFS(graph, start)
maxPathLength   = max(len(p) for p in paths)-1

print("Max Path Length is: {}".format(maxPathLength))

forestMap = []
for line in lines:
    forestMap.append(line.replace("\n", "").replace("<",".").replace(">", ".").replace("^",".").replace("v","."))
    
nbRows = len(forestMap)
nbCols = len(forestMap[0])

start = (0, 1)
end = (nbRows-1, nbCols-2)

graph = defaultdict(list)
directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(nbRows):
    for j in range(nbCols):
        if forestMap[i][j]==".":
            for direction in [(1,0),(-1,0),(0,1),(0,-1)]:
                if i+direction[0] > -1 and i+direction[0] < nbRows and j+direction[1] > -1 and j+direction[1] < nbCols:
                    if forestMap[i+direction[0]][j+direction[1]]==".":
                        graph[(i,j)].append(((i+direction[0], j+direction[1]), 1))
                        
lenRemove = 1
while lenRemove != 0:
    nodesToRemove = []
    for node in graph:
        if len(graph[node]) == 2:
            nodePrev = graph[node][0][0]
            nodeNext = graph[node][1][0]
            lengthPrev = graph[node][0][1]
            lengthNext = graph[node][1][1]
            
            graph[nodePrev].append((nodeNext, lengthPrev+lengthNext))
            graph[nodeNext].append((nodePrev, lengthPrev+lengthNext))
            graph[nodePrev].remove((node, lengthPrev))
            graph[nodeNext].remove((node, lengthNext))
            nodesToRemove.append(node)
    for node in nodesToRemove:
        del graph[node]
    lenRemove = len(nodesToRemove)

def DFS(G,v,seen=None,path=None):
    if seen is None: 
        seen = set()
    if path is None: 
        path = [v[0]]

    seen.add(v[0])

    paths = []
    for t in G[v[0]]:
        if t[0] not in seen:
            t_path = path + [t]
            paths.append(t_path)
            paths.extend(DFS(G, t, copy.copy(seen), t_path))
    return paths
    
def lengthsPaths(paths, end):
    lengths = []
    for path in paths:
        if path[-1][0]==end:
            length = 0
            for node in path:
                length += node[1]
            lengths.append(length)
    return lengths

start = ((0,1),1)
paths = DFS(graph, start)

lengths = lengthsPaths(paths, end)
maxLength = max(lengths)-1

print("Max Path Length is: {}".format(maxLength))
