'''
Link        : https://www.acmicpc.net/problem/10809
Difficulty  : BRONZE-2
Category    : 구현, 문자열
Title       : 알파벳 찾기
'''

import sys

s = sys.stdin.readline().rstrip()

for i in range(97, 123):
    print(s.find(chr(i)), end=' ')