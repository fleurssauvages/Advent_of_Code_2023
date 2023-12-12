#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day4.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
sum = 0
for line in lines:
    line = re.sub(r'[^\w\s]', '', line)
    data = line.split()
    winningNumbers = data[2:12]
    myNumbers = data[12::]
    
    nbMatchingNumbers = len(set(winningNumbers) & set(myNumbers))
    if nbMatchingNumbers > 0:
        sum += pow(2, (nbMatchingNumbers-1))
    
print("Cards sum is: {}".format(sum))

#Q2
nbEachCard = [1]*len(lines)
for i, line in enumerate(lines):
    line = re.sub(r'[^\w\s]', '', line)
    data = line.split()
    winningNumbers = data[2:12]
    myNumbers = data[12::]
    nbMatchingNumbers = len(set(winningNumbers) & set(myNumbers))
    
    if nbMatchingNumbers > 0:
        newNbCards = [np.sum(x) for x in zip(nbEachCard[i+1:(i+nbMatchingNumbers+1)], [nbEachCard[i]]*nbMatchingNumbers)]
        nbEachCard[i+1:(i+nbMatchingNumbers+1)] = newNbCards

print("Number of cards is: {}".format(np.sum(nbEachCard)))