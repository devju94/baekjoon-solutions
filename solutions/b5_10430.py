'''
Link        : https://www.acmicpc.net/problem/10430
Difficulty  : BRONZE-5
Category    : 수학, 구현, 사칙연산
Title       : 나머지
'''

import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)