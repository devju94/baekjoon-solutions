'''
Link        : https://www.acmicpc.net/problem/11720
Difficulty  : BRONZE-2
Category    : 수학, 문자열, 사칙연산
Title       : 숫자의 합
'''

import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

sum = 0
for i in range(n):
    sum += int(s[i])

print(sum)