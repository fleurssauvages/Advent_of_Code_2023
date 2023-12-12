#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day5.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
seeds = lines[0].split()[1::]
seeds = list(map(int, seeds))
isMapped = [0]*len(seeds)

for line in lines[2::]:
    words = line.split()
    if len(words)==0:
        isMapped = [0]*len(seeds)
    if len(words)==3:
        numbers = list(map(int, words))
        for i, seed in enumerate(seeds):
            if isMapped[i] == 0:
                end = numbers[0]
                start = numbers[1]
                rangeOf = numbers[2]
                if (seed >= start) and (seed < start + rangeOf):
                    seeds[i] = seed + end-start
                    isMapped[i] = 1

print("Minimum location is: {}".format(np.min(seeds)))

#Q2
seeds = lines[0].split()[1::]
seeds = list(map(int, seeds))

seedsStart = seeds[0::2]
seedsRange = seeds[1::2]
isMapped = [0]*len(seedsStart)

for line in lines[2::]:
    words = line.split()
    if len(words)==0:
        isMapped = [0]*len(seedsStart)
    if len(words)==3:
        numbers = list(map(int, words))
        for i, (seedStart, seedRange) in enumerate(zip(seedsStart, seedsRange)):
            if isMapped[i] == 0:
                end = numbers[0]
                start = numbers[1]
                rangeOf = numbers[2]
                if (seedStart >= start) and (seedStart+seedRange < start + rangeOf): #Departure is fully included in arrival
                    seedsStart[i] = seedStart + end-start
                    seedsRange[i] = seedRange
                    isMapped[i] = 1
                elif(seedStart < start) and (seedStart+seedRange > start+rangeOf): #Arrival is fully included in departure
                    seedsStart[i] = end
                    seedsRange[i] = rangeOf
                    isMapped[i] = 1
                    seedsStart.append(seedStart) #Append rest on the left
                    seedsRange.append(start-seedStart-1)
                    isMapped.append(0)
                    seedsStart.append(start+rangeOf) #Append rest on the right
                    seedsRange.append(seedStart+seedRange - (start+rangeOf)-1)
                    isMapped.append(0)
                elif(seedStart >= start) and (seedStart < start + rangeOf): #Departure is partly included in arrival on the right
                    seedsStart[i] = seedStart + end-start
                    seedsRange[i] = start+rangeOf-seedStart
                    isMapped[i] = 1
                    seedsStart.append(start+rangeOf) #Append rest on the right
                    seedsRange.append(seedStart+seedRange - (start+rangeOf)-1)
                    isMapped.append(0)
                elif(seedStart < start) and (seedStart+seedRange >= start): #Departure is partly included in arrival on the left
                    seedsStart[i] = end
                    seedsRange[i] = seedRange-(start-seedStart)
                    isMapped[i] = 1
                    seedsStart.append(seedStart) #Append rest on the left
                    seedsRange.append(start-seedStart-1)
                    isMapped.append(0)

print("Minimum range location is: {}".format(np.min(seedsStart)))