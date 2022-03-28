'''
Link        : https://www.acmicpc.net/problem/10869
Difficulty  : BRONZE-5
Category    : 수학, 구현, 사칙연산
Title       : 사칙연산
'''

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)