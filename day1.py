#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day1.txt", "r")
lines = f.readlines()

calibration = 0
for line in lines:
    numbers = re.findall(r'\d', line)  #Regex Directly finds all digits (d)
    number1 = numbers[0]
    number2 = numbers[-1]
    twodigitnumber = int(number1+number2)
    calibration += twodigitnumber
print("Calibration value is: {}".format(calibration))

calibration = 0
numbers = r"""(?=(\d|one|two|three|four|five|six|seven|eight|nine))"""
#Regex finds all digits (d), as well as all keywords. ?= signify that there might be overlap
digitDict = {
    'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0',
    '1': '1','2': '2','3': '3','4': '4','5': '5','6': '6','7': '7','8': '8','9': '9','0': '0'
} #Convert both digits and wods to digits, so we don't have to check if it is int or word

for line in lines:
    numbersDigit = re.findall(numbers, line)
    number1 = digitDict[numbersDigit[0]]
    number2 = digitDict[numbersDigit[-1]]
    twodigitnumber = int(number1+number2)
    calibration += twodigitnumber
print("New Calibration is: {}".format(calibration))