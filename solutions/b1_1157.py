'''
Link        : https://www.acmicpc.net/problem/1157
Difficulty  : BRONZE-1
Category    : 구현, 문자열
Title       : 단어 공부
'''

import sys

s = sys.stdin.readline().rstrip().upper()

alphabetDict = dict()
for c in s:
    if(c in alphabetDict):
        alphabetDict[c] += 1
    else:
        alphabetDict[c] = 1

maxCnt = max(alphabetDict.values())
if(list(alphabetDict.values()).count(maxCnt) > 1):
    print('?')
else:
    print([k for k, v in alphabetDict.items() if v == maxCnt][0])