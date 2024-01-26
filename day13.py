#!/usr/bin/env python3
from collections import defaultdict
import numpy as np

f = open("ressources/day13.txt", "r") #Open File
lines = f.readlines() #Separate in lines

mirrorsRooms = [];

#Gather Data
mirrors = []
for line in lines:
    if len(line.replace("\n", "")) < 2:
        mirrorsRooms.append(mirrors)
        mirrors = []
    else:
        line = line.replace("\n", "")
        mirrors.append(list(line))
mirrorsRooms.append(mirrors)

#Get transpose to solve lines and columns the same way
def transpose(x):
	return list(map(list, zip(*x)))

#Check Symmetry among Lines, tranpose to do the same with columns
def checkSymmetry(x):
    for i in range(1, len(x)):
        patternLength = min(i, len(x)-i)
        pattern1 = x[i-patternLength:i][::-1]
        pattern2 = x[i:i+patternLength]
        if pattern1 == pattern2:
            return i
    return 0
        
def findReflection(x):
    #Check Lines
    symmetryLine = checkSymmetry(x)
    if symmetryLine > 0:
        return symmetryLine*100
    #Check Columns
    return checkSymmetry(transpose(x))

nbRefections = 0
for mirrors in mirrorsRooms:
    nbRefections += findReflection(mirrors)
    
print("Sum of Reflections is: {}".format(nbRefections))

def checkDistance(x):
    for i in range(1, len(x)):
        patternLength = min(i, len(x)-i)
        pattern1 = x[i-patternLength:i][::-1]
        pattern2 = x[i:i+patternLength]
        
        distance = 0
        for p in zip(pattern1, pattern2):
            for pi in zip(p[0],p[1]):
                distance += 1 - (pi[0]==pi[1])
        if distance == 1:
            return i
    return 0

def findReflectionWithSmudge(x):
    #Check Lines
    symmetryLine = checkDistance(x)
    if symmetryLine > 0:
        return symmetryLine*100
    #Check Columns
    return checkDistance(transpose(x))

nbRefections = 0
for mirrors in mirrorsRooms:
    nbRefections += findReflectionWithSmudge(mirrors)
    
print("Sum of Smudged Reflections is: {}".format(nbRefections))