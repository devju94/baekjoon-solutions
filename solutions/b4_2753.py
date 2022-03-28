'''
Link        : https://www.acmicpc.net/problem/2753
Difficulty  : BRONZE-4
Category    : 수학, 구현
Title       : 윤년
'''

import sys

year = int(sys.stdin.readline().rstrip())

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print(1)
else:
    print(0)