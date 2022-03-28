'''
Link        : https://www.acmicpc.net/problem/1546
Difficulty  : BRONZE-1
Category    : 수학, 사칙연산
Title       : 평균
'''

import sys

n = int(sys.stdin.readline().rstrip())
inputDataList = list(map(int, sys.stdin.readline().rstrip().split()))

maxValue = max(inputDataList)
for i in range(len(inputDataList)):
    inputDataList[i] = inputDataList[i] / maxValue * 100

print(sum(inputDataList) / n)