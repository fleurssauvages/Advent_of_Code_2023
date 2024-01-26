#!/usr/bin/env python3
import numpy as np
from collections import defaultdict
import random, copy
import networkx as nx

f = open("ressources/day25.txt", "r") #Open File
lines = f.readlines() #Separate in lines
graph = defaultdict(dict)

for line in lines:
    instructions = line.replace("\n", "").replace(":", "").split(" ")
    name = instructions[0]
    for instruction in instructions[1:]:
        graph[name][instruction] = {'weight': 1}

G = nx.from_dict_of_dicts(graph)
res = next(nx.community.girvan_newman(G))

print("Product of sub-set lengths is: {}".format(len(res[0]) * len(res[1])))