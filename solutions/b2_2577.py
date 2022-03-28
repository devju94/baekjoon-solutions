'''
Link        : https://www.acmicpc.net/problem/2577
Difficulty  : BRONZE-2
Category    : 수학, 사칙연산
Title       : 숫자의 개수
'''

import sys

inputDataList = list()
for i in range(3):
    inputDataList.append(int(sys.stdin.readline().rstrip()))

a = inputDataList[0]
b = inputDataList[1]
c = inputDataList[2]

n = a * b * c

for i in range(10):
    print(str(n).count(str(i)))