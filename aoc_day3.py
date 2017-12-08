#!/usr/bin/python3

import math
import collections


print("Day 3")
print("Exercice 1")
index=312051
step=1
squareSize=1
lenght=0
# Use sqrt()+1 better result
while (squareSize<index):
    step+=2
    squareSize=step*step
    lenght+=1

distanceFromEndOfSquare=squareSize-index
Y=0
X=0
middleVal=squareSize-((step-1)/2)
if(distanceFromEndOfSquare<step-1):
    Y=lenght
    X=-(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*2):
    middleVal-=(step-1)
    X=-lenght
    Y=-(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*3):
    middleVal-=(step-1)*2
    Y=-lenght
    X=(middleVal-index)
elif(distanceFromEndOfSquare<(step-1)*4):
    middleVal-=(step-1)*3
    X=lenght
    Y=(middleVal-index)

Sum=int(abs(X)+abs(Y))
print("Solution:  "+str(Sum))

print("Exercice 2")

def computeCoord(index):
    step=1
    squareSize=1
    lenght=0
    while (squareSize<index):
        step+=2
        squareSize=step*step
        lenght+=1
    distanceFromEndOfSquare=squareSize-index
    Y=0
    X=0
    middleVal=squareSize-((step-1)/2)
    if(distanceFromEndOfSquare<step-1):
        X=lenght
        Y=-(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*2):
        middleVal-=(step-1)
        Y=-lenght
        X=-(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*3):
        middleVal-=(step-1)*2
        X=-lenght
        Y=(middleVal-index)
    elif(distanceFromEndOfSquare<(step-1)*4):
        middleVal-=(step-1)*3
        Y=lenght
        X=(middleVal-index)
    return [X,Y]

def sumAround(matrix,x,y):
    one=matrix[x-1][y-1] if x-1>=0 and y-1>0 else 0
    two=matrix[x][y-1] if  y-1>=0 else 0
    tree=matrix[x+1][y-1] if x+1<len(matrix)  and y-1>=0 else 0
    four=matrix[x-1][y] if x-1>=0 else 0
    five=matrix[x+1][y] if x+1<len(matrix) else 0
    six=matrix[x-1][y+1] if x-1>=0 and y+1<len(matrix[x-1]) else 0
    seven=matrix[x][y+1] if x>=0 and y+1<len(matrix[x-1]) else 0
    eight=matrix[x+1][y+1] if x+1<len(matrix) and y+1<len(matrix[x-1]) else 0
    matrix[x][y] = one+two+tree+four+five+six+seven+eight

size=1
index = 312051
validMatrix=[]
lastValue=1
while lastValue<index:
    size+=2
    matrix = [[0 for i in range(0,size)] for i in range(0,size)]
    middle=int(size/2)
    matrix[middle][middle]=1
    for i in range(2,size*size+1):
        coord = computeCoord(i)
        sumAround(matrix,middle+int(coord[0]),middle+int(coord[1]))
    lastValue=matrix[size-1][size-1]
    validMatrix=matrix
dico = {}
for line in matrix:
    for value in line:
        if(value > index):
            dico[value-index]=value
a = sorted(dico.items())[0]
print("Solution: "+str(a[1]))

