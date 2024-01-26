#!/usr/bin/env python3
from collections import defaultdict
import numpy as np
import re
import heapq as hp
import time

f = open("ressources/day17.txt", "r") #Open File
lines = f.readlines() #Separate in lines

heatMap = []
for line in lines:
    heatMap.append([int(x) for x in list(line.replace("\n", ""))])

def dijkstra(heatMap, minStep, maxStep):
    nbRows = len(heatMap)
    nbCols = len(heatMap[0])
    
    seenNodes = set()
    djikstraMap = defaultdict(int)
    queueNodes = [(0,[0,0,0,(1,0)]),(0,[0,0,0,(0,1)])] #A node is x, y, nbSteps, direction in x, direction in y
    
    target = (nbRows-1,nbCols-1)
    
    while len(queueNodes):
        cost, currentNode = hp.heappop(queueNodes) #Get next in queue
        if str(currentNode) in seenNodes: #If already seen, skip
            continue
        seenNodes.add(str(currentNode)) #If not, add it to seen
        if (currentNode[0], currentNode[1]) == target: #Check if arrived with minimum number of steps
            if currentNode[2] >= minStep:
                return djikstraMap[str(currentNode)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        directions.remove((-currentNode[3][0], -currentNode[3][1])) #Cannot go backward
        if currentNode[2] == maxStep: #If maximum number of steps has been done, cannot keep going in that direction
            directions.remove((currentNode[3][0], currentNode[3][1]))
        if currentNode[2] < minStep: #If minimum number of steps has not been done, keep going
            directions = [(currentNode[3][0], currentNode[3][1])]
        for direction in directions: #Take a step
            x = currentNode[0] + direction[0]
            y = currentNode[1] + direction[1]
            nbSteps = 1 + currentNode[2]*((currentNode[3][0], currentNode[3][1])==direction)
            if x > -1 and y > -1 and x < nbRows and y < nbCols: #Check if you are still inside the board
                newNode = [x,y,nbSteps,(direction[0],direction[1])]
                if str(newNode) in seenNodes: #Check if you have not visited this place yet
                    continue
                cost = djikstraMap[str(currentNode)] + heatMap[x][y]
                if cost < djikstraMap[str(newNode)] or djikstraMap[str(newNode)] == 0: #Check if you have a smaller cost
                    djikstraMap[str(newNode)] = cost #In that case, update
                    hp.heappush(queueNodes,(cost,newNode)) #Add you current state to the queue
    return djikstraMap

dijkstraValue = dijkstra(heatMap,1,3)
print("Minimal Heat Loss is: {}".format(dijkstraValue))
dijkstraValue = dijkstra(heatMap,4,10)
print("Minimal Heat Loss is: {}".format(dijkstraValue))