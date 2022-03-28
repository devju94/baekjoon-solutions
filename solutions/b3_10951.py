'''
Link        : https://www.acmicpc.net/problem/10951
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : A+B - 4
'''

import sys

while(True):
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except:
        break