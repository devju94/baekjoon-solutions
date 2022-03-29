'''
Link        : https://www.acmicpc.net/problem/1541
Difficulty  : SILVER-2
Category    : 수학, 문자열, 그리디 알고리즘, 파싱
Title       : A+B - 5
'''

import sys 

input = sys.stdin.readline().rstrip()
num = []

minusTokens = input.split('-')
for mToken in minusTokens:
    cnt = 0
    plusTokens = mToken.split('+')
    for pToken in plusTokens:
        cnt += int(pToken)
    num.append(cnt)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)