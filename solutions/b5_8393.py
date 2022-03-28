'''
Link        : https://www.acmicpc.net/problem/8393
Difficulty  : BRONZE-5
Category    : 수학, 구현
Title       : 합
'''

import sys

n = int(sys.stdin.readline().rstrip())

sum = 0
for i in range(1, n+1):
    sum = sum + i

print(sum)