'''
Link        : https://www.acmicpc.net/problem/2438
Difficulty  : BRONZE-3
Category    : 구현
Title       : 별 찍기 - 1
'''

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    for j in range(i+1):
        print('*', end='')
    print('')