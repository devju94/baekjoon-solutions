'''
Link        : https://www.acmicpc.net/problem/14681
Difficulty  : BRONZE-4
Category    : 수학, 구현, 기하학
Title       : 사분면 고르기
'''

import sys

inputDataList = list()
for i in range(2):
    inputDataList.append(int(sys.stdin.readline().rstrip()))

x = inputDataList[0]
y = inputDataList[1]

if((x > 0) and (y > 0)):
    print(1)
elif((x < 0) and (y > 0)):
    print(2)
elif((x < 0) and (y < 0)):
    print(3)
else:
    print(4)