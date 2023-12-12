#!/usr/bin/env python3
import numpy as np

f = open("ressources/day9.txt", "r") #Open File
lines = f.readlines() #Separate in lines

def extrapolate(numbers):
    extrapolation = numbers[-1]
    while np.sum(np.abs(numbers)) > 0:
        numbers = [x[0]-x[1] for x in zip(numbers[1::], numbers[0:-1:])]
        extrapolation += numbers[-1]
    return extrapolation

extrapolationsEnd, extrapolationsStart = [], []
for line in lines:
    numbers = [int(x) for x in line.split()]
    extrapolationsEnd.append(extrapolate(numbers))
    
    numbers.reverse()
    extrapolationsStart.append(extrapolate(numbers))
    
print("Sum of End extrapolation is: {}".format(np.sum(extrapolationsEnd)))
print("Sum of Beginning extrapolation is: {}".format(np.sum(extrapolationsStart)))