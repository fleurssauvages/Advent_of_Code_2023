#!/usr/bin/env python3
import numpy as np
import copy

f = open("ressources/day19.txt", "r") #Open File
lines = f.readlines() #Separate in lines

class Instruction():
    def __init__(self, letter, symbol="=", value=0, do="out"):
        self.letter = letter
        self.symbol = symbol
        self.value = value
        self.do = do
    def evaluate(self, part):
        if self.letter == "A":
            return "A"
        if self.letter == "R":
            return "R"
        if self.letter not in "xmas":
            return self.letter

        numbers = {"x":0, "m":1, "a":2, "s":3}
        number = numbers[self.letter]
        if self.symbol == "<":
            if part[number] < self.value:
                return self.do
        if self.symbol == ">":
            if part[number] > self.value:
                return self.do
        return -1
            
class Workflow():
    def __init__(self, instructions):
        self.instructions = instructions
    def evaluate(self, part):
        for instruction in self.instructions:
            evaluation = instruction.evaluate(part)
            if evaluation == "A":
                return np.sum(part)
            elif evaluation == "R":
                return 0
            elif evaluation == -1:
                continue
            else:
                return evaluation
            
def evaluate(workflows, part):
    value = "in"
    while not isinstance(value, int):
        workflow = workflows[value]
        value = workflow.evaluate(part)
    return value

#Reading Workflows, first part of input
workflows = {}
for i, line in enumerate(lines):
    if len(line) < 3:
        break
    line = line.replace("\n", "").replace("{",",").replace("}", "").replace("<", ",<,").replace(">", ",>,").replace(":",",")
    instructionsValues = line.split(",")
    
    name = instructionsValues[0]
    letters = instructionsValues[1::4]
    symbol = instructionsValues[2::4]
    value = instructionsValues[3::4]
    do = instructionsValues[4::4]
    
    instructions = []
    for l,s,v,d in zip(letters,symbol,value,do):
        instructions.append(Instruction(l,s,int(v),d))
    instructions.append(Instruction(letters[-1]))
    workflow = Workflow(instructions)
    workflows[name] = workflow

#Reading parts, second part of input
parts = [] 
for line in lines[i+1:]:
    line = line.replace("\n", "").replace("{","").replace("}", "").replace("=",",")
    line = line.split(",")
    
    symbols = line[0::2]
    values = line[1::2]
    values = [int(value) for value in values]
    parts.append(values)
sum = 0

# Part 1
#Evaluating the parts
for part in parts:
    sum += evaluate(workflows, part)
print("Sum of accepted parts is: {}".format(sum))

# Part 2
def evaluateCombination(splits, workflowname, workflows):
    sum = 0

    for instruction in workflows[workflowname].instructions:
        letter = instruction.letter
        value = instruction.value
        
        if ">"==instruction.symbol:
            new_splits = copy.deepcopy(splits)
            if new_splits[letter][1] > value:
                new_splits[letter][0] = max(new_splits[letter][0], value+1)
                if instruction.do == "A":
                    sum += np.prod([ranging[1]-ranging[0]+1 for ranging in new_splits.values()])
                elif instruction.do != "R":
                    sum += evaluateCombination(new_splits, instruction.do, workflows)
                splits[letter][1] = min(splits[letter][1], value)
                
        elif "<"==instruction.symbol:
            new_splits = copy.deepcopy(splits)
            if new_splits[letter][0] < value:
                new_splits[letter][1] = min(new_splits[letter][1], value-1)
                if instruction.do == "A":
                    sum += np.prod([ranging[1]-ranging[0]+1 for ranging in new_splits.values()])
                elif instruction.do != "R":
                    sum += evaluateCombination(new_splits, instruction.do, workflows)
                splits[letter][0] = max(splits[letter][0], value)
        else:
            if instruction.letter == "A":
                sum += np.prod([ranging[1]-ranging[0]+1 for ranging in splits.values()])
            elif instruction.letter == "R":
                continue
            else:
                sum += evaluateCombination(splits, instruction.letter, workflows)
                
    return sum

splits = {}
splits['x'] = [1, 4000]
splits['m'] = [1, 4000]
splits['a'] = [1, 4000]
splits['s'] = [1, 4000]
sum = evaluateCombination(splits, "in", workflows)
print("Sum of accepted parts is: {}".format(sum))