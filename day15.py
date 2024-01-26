#!/usr/bin/env python3
from collections import defaultdict
import numpy as np
import re

f = open("ressources/day15.txt", "r") #Open File
lines = f.readlines() #Separate in lines

def hash(numbers):
    code = 0
    for number in numbers:
        code += number
        code *= 17
        code %= 256
    return code

words = lines[0].split(',')

sum =0
for word in words:
    asciiCode = [ord(char) for char in word]
    hashCode = hash(asciiCode)
    sum += hashCode

print("Sum of Hash Codes is: {}".format(int(sum)))

boxesLabels = defaultdict(list)
boxesFocals = defaultdict(list)

instructions = lines[0].split(',')
for instruction in instructions:
    if '=' in instruction:
        focal = int(instruction[-1])
        label = instruction[:-2]
        asciiCode = [ord(char) for char in label]
        hashCode = hash(asciiCode)
        
        if label in boxesLabels[hashCode]:
            idx = boxesLabels[hashCode].index(label)
            boxesFocals[hashCode][idx] = focal
        else:
            boxesLabels[hashCode].append(label)
            boxesFocals[hashCode].append(focal)
        
    if '-' in instruction:
        label = instruction[:-1]
        asciiCode = [ord(char) for char in label]
        hashCode = hash(asciiCode)
        
        if label in boxesLabels[hashCode]:
            idx = boxesLabels[hashCode].index(label)
            boxesFocals[hashCode].pop(idx)
            boxesLabels[hashCode].pop(idx)

sum = 0
for boxNumber, focals in zip(boxesFocals.keys(), boxesFocals.values()):
    for i, focal in enumerate(focals):
        sum += (boxNumber+1)*(i+1)*focal

print("Sum of Focal Codes is: {}".format(int(sum)))