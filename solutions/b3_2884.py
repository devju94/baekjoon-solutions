'''
Link        : https://www.acmicpc.net/problem/2884
Difficulty  : BRONZE-3
Category    : 수학, 사칙연산
Title       : 알람 시계
'''

import sys

H, M = map(int, sys.stdin.readline().rstrip().split())

if(M < 45):
    M = 60 - (45 - M)
    if(H == 0):
        H = 23
    else:
        H = H - 1
else:
    M = M - 45

print("%d %d" %(H, M))