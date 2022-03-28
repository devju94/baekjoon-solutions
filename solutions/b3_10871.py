'''
Link        : https://www.acmicpc.net/problem/10871
Difficulty  : BRONZE-3
Category    : 수학, 구현
Title       : X보다 작은 수
'''

import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
inputDataList = list(map(int, sys.stdin.readline().rstrip().split()))

for data in inputDataList:
    if(data < X):
        print(data, end=' ')