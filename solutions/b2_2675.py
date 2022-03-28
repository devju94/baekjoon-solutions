'''
Link        : https://www.acmicpc.net/problem/2675
Difficulty  : BRONZE-2
Category    : 구현
Title       : 문자열 반복
'''

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    r, s = map(str, sys.stdin.readline().rstrip().split())

    for i in s:
        for j in range(int(r)):
            print(i, end='')
    
    print('')