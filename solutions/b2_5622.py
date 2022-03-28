'''
Link        : https://www.acmicpc.net/problem/5622
Difficulty  : BRONZE-2
Category    : 구현
Title       : 다이얼
'''

import sys

s = sys.stdin.readline().rstrip()

time = 3
check = 0
alphabet = 65
timeDict = dict()
for i in range(2, 10):
    if(i == 7 or i == 9):
        repeat = 4
    else:
        repeat = 3
    
    for j in range(repeat):
        timeDict[chr(alphabet + check)] = time
        check += 1
    
    time += 1

timeSum = 0
for i in s:
    timeSum += timeDict[i]
    
print(timeSum)