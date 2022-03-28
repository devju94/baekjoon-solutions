'''
Link        : https://www.acmicpc.net/problem/11021
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : A+B - 7
'''

import sys

T = int(sys.stdin.readline().rstrip())

inputDataList = list()
for i in range(T):
    inputDataList.append(list(map(int, sys.stdin.readline().rstrip().split())))

caseNumber = 1
for data in inputDataList:
    print('Case #%d: %d' %(caseNumber, data[0] + data[1]))
    caseNumber += 1