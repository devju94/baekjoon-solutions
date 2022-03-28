'''
Link        : https://www.acmicpc.net/problem/1110
Difficulty  : BRONZE-1
Category    : 수학, 구현
Title       : 더하기 사이클
'''

import sys

n = int(sys.stdin.readline().rstrip())

newN = n
cycleLength = 0
while(True):
    cycleLength += 1

    if(newN < 10):
        newN = (newN * 10) + newN
    else:
        newN = ((newN % 10) * 10) + (((newN // 10) + (newN % 10)) % 10)

    if(newN == n):
        break

print(cycleLength)