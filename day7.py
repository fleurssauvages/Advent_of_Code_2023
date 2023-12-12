#!/usr/bin/env python3
import numpy as np
from collections import Counter
from functools import cmp_to_key

f = open("ressources/day7.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
hands = [];

for line in lines:
    words = line.split()
    hands.append((words[0], words[1]))

stringToValue = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T':10, 
                '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    
def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    
    counter1 = Counter(hand1)
    counter2 = Counter(hand2)
    
    minNumberToCheck = min(len(counter1.most_common()), len(counter2.most_common()))
    for i in range(minNumberToCheck):
        if counter1.most_common()[i][1] != counter2.most_common()[i][1]:
            return counter1.most_common()[i][1] - counter2.most_common()[i][1]
    for i in range(5):
        if stringToValue[hand1[i]] != stringToValue[hand2[i]]:
            return stringToValue[hand1[i]] - stringToValue[hand2[i]]

# Sorting
hands.sort(key=cmp_to_key(compare))
sortedBids = [int(x[1]) for x in hands]
winning = np.sum(np.multiply(list(range(1, len(hands)+1, 1)), sortedBids))
print("Total winning is: {}".format(winning))

#Q2
stringToValue = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T':10, 
                '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    
def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    
    counter1 = Counter(hand1)
    counter2 = Counter(hand2)
    
    nbJ1 = counter1['J']
    nbJ2 = counter2['J']
    counter1['J'] = 0
    counter2['J'] = 0
    
    minNumberToCheck = min(len(counter1.most_common()), len(counter2.most_common()))
    for i in range(minNumberToCheck):
        if counter1.most_common()[i][1] + nbJ1*(i==0) != counter2.most_common()[i][1] + nbJ2*(i==0):
            return counter1.most_common()[i][1] + nbJ1*(i==0) - (counter2.most_common()[i][1] + nbJ2*(i==0))
    for i in range(5):
        if stringToValue[hand1[i]] != stringToValue[hand2[i]]:
            return stringToValue[hand1[i]] - stringToValue[hand2[i]]

# Sorting
hands.sort(key=cmp_to_key(compare))
sortedBids = [int(x[1]) for x in hands]
winning = np.sum(np.multiply(list(range(1, len(hands)+1, 1)), sortedBids))
print("Total winning is: {}".format(winning))