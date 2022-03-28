'''
Link        : https://www.acmicpc.net/problem/2739
Difficulty  : BRONZE-3
Category    : 수학, 구현, 사칙연산
Title       : 구구단
'''

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print('%d * %d = %d' %(n, i, n*i))