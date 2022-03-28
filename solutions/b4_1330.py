'''
Link        : https://www.acmicpc.net/problem/1330
Difficulty  : BRONZE-4
Category    : 수학, 구현, 사칙연산
Title       : 두 수 비교하기
'''

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if(a > b):
    print('>')
elif(a < b):
    print('<')
else:
    print('==')