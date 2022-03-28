'''
Link        : https://www.acmicpc.net/problem/3052
Difficulty  : BRONZE-2
Category    : 수학, 사칙연산
Title       : 나머지
'''

import sys

inputDataList = list()
for i in range(10):
    inputDataList.append(int(sys.stdin.readline().rstrip()))

resultList = list()
for data in inputDataList:
    resultList.append(data % 42)

resultSet = set(resultList)
print(len(resultSet))