'''
Link        : https://www.acmicpc.net/problem/2742
Difficulty  : BRONZE-3
Category    : 구현
Title       : 기찍 N
'''

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n, 0, -1):
    print(i)