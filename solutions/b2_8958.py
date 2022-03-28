'''
Link        : https://www.acmicpc.net/problem/8958
Difficulty  : BRONZE-2
Category    : 구현, 문자열
Title       : OX퀴즈
'''

import sys

T = int(sys.stdin.readline().rstrip())
inputDataList = list()
for i in range(T):
    inputDataList.append(sys.stdin.readline().rstrip())

for data in inputDataList:
    prev = ''
    probPoint = 0
    scoreSum = 0

    for prob in data:
        if(prob == 'O'):
            if(prev == 'O'):
                probPoint += 1
            else:
                probPoint = 1
            scoreSum += probPoint
            prev = 'O'
        else:
            prev = 'X'

    print(scoreSum)