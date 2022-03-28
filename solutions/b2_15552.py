'''
Link        : https://www.acmicpc.net/problem/15552
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : 빠른 A+B
'''

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)