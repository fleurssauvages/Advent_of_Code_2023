#!/usr/bin/env python3
import numpy as np
from itertools import combinations

class HailParticle:
    def __init__(self, point, velocity):
        self.px, self.py, self.pz, self.vx, self.vy, self.vz = point[0], point[1], point[2], velocity[0], velocity[1], velocity[2]
        if self.vx == 0:
            self.slope = "inf"
        else:
            self.slope = self.vy/self.vx
    
    def intersection(self, other):
        if self.slope==other.slope: #Colinear Case
            return None
        if self.slope == "inf": #Vertical case 1
            intersectionX = self.px
            intersectionY = other.slope * (intersectionX - other.px) + other.py
        elif other.slope == "inf": #Vertical case 2
            intersectionX = other.px
            intersectionY = self.slope * (intersectionX - self.px) + self.py
        else: #General Case
            intersectionX = (self.py-other.py  - self.px*self.slope + other.px*other.slope)/(other.slope-self.slope)
            intersectionY = self.py + self.slope*(intersectionX-self.px)
        
        if np.sign(intersectionX-self.px) != np.sign(self.vx): #Check that line crosses in the vx direction and not oppositve
            return None
        if np.sign(intersectionX-other.px) != np.sign(other.vx):
            return None

        return (intersectionX, intersectionY)


f = open("ressources/day24.txt", "r") #Open File
lines = f.readlines() #Separate in lines
hailParticles = {}
for i, line in enumerate(lines):
    instructions = line.replace("\n", "").replace("@", ",").split(",")
    x, y, z = float(instructions[0]), float(instructions[1]), float(instructions[2])
    vx, vy, vz = float(instructions[3]), float(instructions[4]), float(instructions[5])
    hailParticles[i] = HailParticle((x,y,z), (vx, vy, vz))

testMin = 200000000000000
testMax = 400000000000000
nbIntersectionsInTest = 0

intersections = [hailParticles[i].intersection(hailParticles[j]) for i,j in combinations(hailParticles, 2)]
    
for intersection in intersections:
    if intersection is None:
        continue
    elif intersection[0] >= testMin and intersection[0] <= testMax:
        if intersection[1] >= testMin and intersection[1] <= testMax:
            nbIntersectionsInTest += 1
                    
print("Nb of Intersections is: {}".format(nbIntersectionsInTest))

line1, line2, line3 = lines[3], lines[4], lines[5]
instructions = line1.replace("\n", "").replace("@", ",").split(",")
x, y, z = float(instructions[0]), float(instructions[1]), float(instructions[2])
vx, vy, vz = float(instructions[3]), float(instructions[4]), float(instructions[5])
(p0, v0) = (x,y,z), (vx, vy, vz)

instructions = line2.replace("\n", "").replace("@", ",").split(",")
x, y, z = float(instructions[0]), float(instructions[1]), float(instructions[2])
vx, vy, vz = float(instructions[3]), float(instructions[4]), float(instructions[5])
(p1, v1) = (x,y,z), (vx, vy, vz)

instructions = line3.replace("\n", "").replace("@", ",").split(",")
x, y, z = float(instructions[0]), float(instructions[1]), float(instructions[2])
vx, vy, vz = float(instructions[3]), float(instructions[4]), float(instructions[5])
(p2, v2) = (x,y,z), (vx, vy, vz)

A = np.array([[-(v0[1] - v1[1]), v0[0] - v1[0], 0, p0[1] - p1[1], -(p0[0] - p1[0]), 0],
    [-(v0[1] - v2[1]), v0[0] - v2[0], 0, p0[1] - p2[1], -(p0[0] - p2[0]), 0],

    [0, -(v0[2] - v1[2]), v0[1] - v1[1],  0, p0[2] - p1[2], -(p0[1] - p1[1])],
    [0, -(v0[2] - v2[2]), v0[1] - v2[1],  0, p0[2] - p2[2], -(p0[1] - p2[1])],

    [-(v0[2] - v1[2]), 0, v0[0] - v1[0],  p0[2] - p1[2], 0, -(p0[0] - p1[0])],
    [-(v0[2] - v2[2]), 0, v0[0] - v2[0],  p0[2] - p2[2], 0, -(p0[0] - p2[0])]])

b = [(p0[1] * v0[0] - p1[1] * v1[0]) - (p0[0] * v0[1] - p1[0] * v1[1]),
    (p0[1] * v0[0] - p2[1] * v2[0]) - (p0[0] * v0[1] - p2[0] * v2[1]),

    (p0[2] * v0[1] - p1[2] * v1[1]) - (p0[1] * v0[2] - p1[1] * v1[2]),
    (p0[2] * v0[1] - p2[2] * v2[1]) - (p0[1] * v0[2] - p2[1] * v2[2]),

    (p0[2] * v0[0] - p1[2] * v1[0]) - (p0[0] * v0[2] - p1[0] * v1[2]),
    (p0[2] * v0[0] - p2[2] * v2[0]) - (p0[0] * v0[2] - p2[0] * v2[2])]

x = np.linalg.solve(A, b)
print("Rock sum is: {}".format(int(np.round(np.sum(x[0:3])))))
