#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day2.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
totalPossible = 0
for line in lines:
    line = re.sub(r'[^\w\s]', '', line)
    data = line.split()
    
    isPossible = 1
    for number, color in zip(data[2::2], data[3::2]):
        for match, totalNumber in zip(["red", "green", "blue"], [12,13,14]):
            if match in color:
                if int(number) > totalNumber:
                    isPossible = 0
    totalPossible += isPossible*int(data[1])
print("Number of possible games ID is: {}".format(totalPossible))

#Q2
powerSets = 0
for line in lines:
    line = re.sub(r'[^\w\s]', '', line)
    data = line.split()
    
    numberPerColor = [0,0,0]
    colors = ["red", "green", "blue"]
    
    for number, color in zip(data[2::2], data[3::2]):
        for k in [0,1,2]:
            if color in colors[k]:
                if int(number) > numberPerColor[k]:
                    numberPerColor[k] = int(number)
                    
    powerSets += numberPerColor[0]*numberPerColor[1]*numberPerColor[2]
print("Number of power is: {}".format(powerSets))