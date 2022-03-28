'''
Link        : https://www.acmicpc.net/problem/2908
Difficulty  : BRONZE-2
Category    : 수학, 구현
Title       : 상수
'''

import sys

a, b = map(str, sys.stdin.readline().rstrip().split())

new_a = ''
new_b = ''

for i in range(2, -1, -1):
    new_a += a[i]
    new_b += b[i]

if(int(new_a) > int(new_b)):
    print(new_a)
else:
    print(new_b)