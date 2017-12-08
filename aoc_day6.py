#!/usr/bin/python3

import math
import collections

print("Day 6")


print("Exercice 1")
currentInput = [5,	1,	10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]

def contains(list1,matrix):
    for list in matrix:
        if( list1 == list):
            return True
    return False

previousStep = []
count =0
while (not contains(currentInput,previousStep)):
    count+=1
    previousStep.append(list(currentInput))
    maxVal = max(currentInput)
    index = currentInput.index(maxVal)
    currentInput[index]=0
    index+=1
    while (maxVal > 0):
        if(index>=len(currentInput)):
            index=0
        currentInput[index]+=1
        maxVal-=1
        index+=1

print("Solution: "+str(count))





print("Exercice 2")
currentInput = [5,	1,	10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]

def contains(list1,matrix):
    for list in matrix:
        if( list1 == list):
            return True
    return False

previousStep = []
count =0
while (not contains(currentInput,previousStep)):
    count+=1
    previousStep.append(list(currentInput))

    maxVal = max(currentInput)
    index = currentInput.index(maxVal)
    currentInput[index]=0
    index+=1

    while (maxVal > 0):
        if(index>=len(currentInput)):
            index=0
        currentInput[index]+=1
        maxVal-=1
        index+=1


bigIndex= previousStep.index(currentInput)
size = len(previousStep)
count = size-bigIndex

print("Solution: "+str(count))


