#!/usr/bin/env python3
import numpy as np
from collections import deque, defaultdict

f = open("ressources/day20.txt", "r") #Open File
lines = f.readlines() #Separate in lines

class FlipFlop():
    def __init__(self, name, senders):
        self.name = name
        self.state = 0
        self.senders = senders
        self.nbLowPulses = 0
        self.nbHighPulses = 0
        self.hasToSend = 0
        self.pulseToSend = "low"
    def receive(self, senderName, pulse, modulesList):
        if pulse == "low":
            if self.state:
                pulseToSend = "low"
            else:
                pulseToSend = "high"
            self.state = 1-self.state
            self.pulseToSend = pulseToSend
            self.nbLowPulses += 1
            self.hasToSend += 1
        else:
            self.nbHighPulses += 1
    def send(self, modulesList):
        for sender in self.senders:
            # print(self.name, self.pulseToSend, sender)
            modulesList[sender].receive(self.name, self.pulseToSend, modulesList)
        self.hasToSend -= 1
        return self.senders
                
class Conjuction():
    def __init__(self, name, senders):
        self.name = name
        self.memory = {}
        self.senders = senders
        self.nbLowPulses = 0
        self.nbHighPulses = 0
        self.hasToSend = 0
        self.pulseToSend = "low"
    def receive(self, senderName, pulse, modulesList):
        self.hasToSend += 1
        if pulse == "low":
            self.nbLowPulses += 1
        if pulse == "high":
            self.nbHighPulses += 1
        self.memory[senderName] = pulse
        memoryState  = np.prod([state == "high" for state in self.memory.values()])
        if memoryState:
            self.pulseToSend = "low"
        else:
            self.pulseToSend = "high"
    def send(self, modulesList):
        for sender in self.senders:
            # print(self.name, self.pulseToSend, sender)
            modulesList[sender].receive(self.name, self.pulseToSend, modulesList)
        self.hasToSend -= 1
        return self.senders
                
class Broadcaster():
    def __init__(self, name, senders):
        self.name = name
        self.senders = senders
        self.nbLowPulses = 0
        self.nbHighPulses = 0
        self.hasToSend = 0
        self.pulseToSend = "low"
    def receive(self, senderName, pulse, modulesList):
        if pulse == "low":
            self.nbLowPulses += 1
        if pulse == "high":
            self.nbHighPulses += 1
        self.pulseToSend = pulse
        self.hasToSend += 1
    def send(self, modulesList):
        for sender in self.senders:
            # print(self.name, self.pulseToSend, sender)
            modulesList[sender].receive(self.name, self.pulseToSend, modulesList)
        self.hasToSend -= 1
        return self.senders

class Output():
    def __init__(self, name):
        self.name = name
        self.nbLowPulses = 0
        self.nbHighPulses = 0
        self.senders = []
        self.hasToSend = 0
    def receive(self, name, pulse, modulesList):
        if pulse == "low":
            self.nbLowPulses += 1
        if pulse == "high":
            self.nbHighPulses += 1
    def send(self, modulesList):
        return []

def read(lines):
    modulesList = {}
    for line in lines:
        modules = line.replace("\n", "").replace("->", ",").replace(" ", "").split(",")
        receiver = modules[0]
        senders = modules[1:]
        if receiver[0] == "%":
            name = receiver[1:]
            module = FlipFlop(name, senders)
        elif receiver[0] == "&":
            name = receiver[1:]
            module = Conjuction(name, senders)
        else:
            name = "broadcaster"
            module = Broadcaster(name, senders)
        modulesList[name] = module

    for module in modulesList.values():
        for sender in module.senders:
            try:
                modulesList[sender].memory[module.name] = "low"
            except:
                pass
        for sender in module.senders:
            if sender not in modulesList:
                modulesList[sender] = Output(sender)
    return modulesList

modulesList = read(lines)
for i in range(1000):
    modulesList["broadcaster"].receive("button", "low", modulesList)
    modulesToSend = modulesList["broadcaster"].send(modulesList)
    
    q = deque()
    for module in modulesToSend:
        q.append(module)

    while len(q) > 0:
        module = q.popleft()
        if modulesList[module].hasToSend:
            newModules = modulesList[module].send(modulesList)
            for newModule in newModules:
                q.append(newModule)

nbLowPulses = 0
nbHighPulses = 0
for module in modulesList.values():
    nbLowPulses += module.nbLowPulses
    nbHighPulses += module.nbHighPulses

print("Product of low and high pulses is: {}".format(nbLowPulses*nbHighPulses))

modulesList = read(lines)

rxReceiver = ""
for line in lines:
    modules = line.replace("\n", "").replace("->", ",").replace(" ", "").split(",")
    receiver = modules[0]
    senders = modules[1:]
    if "rx" in senders:
        rxReceiver = modules[0][1:]

conjunctionList = set()
for line in lines:
    modules = line.replace("\n", "").replace("->", ",").replace(" ", "").split(",")
    receiver = modules[0]
    senders = modules[1:]
    if rxReceiver in senders:
        conjunctionList.add(modules[0][1:])

memoriesList = {conjunction :0 for conjunction in conjunctionList}
keepGoing = True

for i in range(10000):
    modulesList["broadcaster"].receive("button", "low", modulesList)
    modulesToSend = modulesList["broadcaster"].send(modulesList)
    
    q = deque()
    for module in modulesToSend:
        q.append(module)

    while len(q) > 0:
        module = q.popleft()
        if modulesList[module].hasToSend:
            newModules = modulesList[module].send(modulesList)
            for newModule in newModules:
                q.append(newModule)
            if module in conjunctionList:
                if modulesList[module].pulseToSend == "high":
                    if memoriesList[module] == 0:
                        memoriesList[module] = i+1
    
    keepGoing = False                 
    for conjunction in memoriesList:
        if memoriesList[conjunction] == 0:
            keepGoing = True

firstPulseNb = np.lcm.reduce([memoriesList[conjunction] for conjunction in memoriesList])
print("First High Pulse arrives at rx at: {}".format(firstPulseNb))