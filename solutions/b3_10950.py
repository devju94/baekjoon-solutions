'''
Link        : https://www.acmicpc.net/problem/10950
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : A+B - 3
'''

import sys

T = int(sys.stdin.readline().rstrip())

inputDataList = list()
for i in range(T):
    inputDataList.append(list(map(int, sys.stdin.readline().rstrip().split())))

for data in inputDataList:
    print(data[0] + data[1])