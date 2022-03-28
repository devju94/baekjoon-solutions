'''
Link        : https://www.acmicpc.net/problem/2439
Difficulty  : BRONZE-3
Category    : 구현
Title       : 별 찍기 - 2
'''

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    for j in range(T-(i+1)):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print('')