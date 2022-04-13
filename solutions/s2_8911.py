'''
Link        : https://www.acmicpc.net/problem/8911
Difficulty  : SILVER-2
Category    : 구현, 시뮬레이션
Title       : 거북이
'''

import sys

T = int(sys.stdin.readline().rstrip())

data = list()
for i in range(T):
    data.append(sys.stdin.readline().rstrip())

def executeCommand(c, currX, currY, currD):
    nextX, nextY, nextD = currX, currY, currD
    if(c == 'F'):
        if(currD == 0):
            nextY = currY + 1
        elif(currD == 1):
            nextX = currX + 1
        elif(currD == 2):
            nextY = currY - 1
        elif(currD == 3):
            nextX = currX - 1
    elif(c == 'B'):
        if(currD == 0):
            nextY = currY - 1
        elif(currD == 1):
            nextX = currX - 1
        elif(currD == 2):
            nextY = currY + 1
        elif(currD == 3):
            nextX = currX + 1
    elif(c == 'L'):
        if(currD == 0):
            nextD = 3
        elif(currD == 1):
            nextD = 0
        elif(currD == 2):
            nextD = 1
        elif(currD == 3):
            nextD = 2
    elif(c =='R'):
        if(currD == 0):
            nextD = 1
        elif(currD == 1):
            nextD = 2
        elif(currD == 2):
            nextD = 3
        elif(currD == 3):
            nextD = 0
    
    return nextX, nextY, nextD
                
for commands in data:
    currX, currY, currD = 0, 0, 0
    nextX, nextY, nextD = 0, 0, 0
    
    path = set()
    for c in commands:
        nextX, nextY, nextD = executeCommand(c, currX, currY, currD)
        path.add((currX,currY))
        path.add((nextX,nextY))
        currX, currY, currD = nextX, nextY, nextD
    
    minX = min(p[0] for p in path)
    minY = min(p[1] for p in path)
    maxX = max(p[0] for p in path)
    maxY = max(p[1] for p in path)
        
    print((maxX - minX) * (maxY - minY))