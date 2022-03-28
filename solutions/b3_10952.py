'''
Link        : https://www.acmicpc.net/problem/10952
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : A+B - 5
'''

import sys

while(True):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if(a == 0 and b == 0):
        break
    else:
        print(a+b)