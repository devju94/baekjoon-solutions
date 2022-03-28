'''
Link        : https://www.acmicpc.net/problem/1712
Difficulty  : BRONZE-4
Category    : 수학, 사칙연산
Title       : 손익분기점
'''

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(int(A//(C-B)+1))