'''
Link        : https://www.acmicpc.net/problem/2562
Difficulty  : BRONZE-2
Category    : 구현
Title       : 최댓값
'''

import sys

inputDataList = list()
for i in range(9):
    inputDataList.append(int(sys.stdin.readline().rstrip()))

maxValue = max(inputDataList)
indexDict = {data: i+1 for i, data in enumerate(inputDataList)}

print(maxValue)
print(indexDict[maxValue])