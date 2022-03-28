'''
Link        : https://www.acmicpc.net/problem/2941
Difficulty  : SILVER-5
Category    : 구현, 문자열
Title       : 크로아티아 알파벳
'''

import sys

s = sys.stdin.readline().rstrip()

croatiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatiaAlphabet:
    s = s.replace(i, '#')

print(len(s))