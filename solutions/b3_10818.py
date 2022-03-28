'''
Link        : https://www.acmicpc.net/problem/10818
Difficulty  : BRONZE-3
Category    : 수학, 구현
Title       : 최소, 최대
'''

import sys

T = int(sys.stdin.readline().rstrip())
inputDataList = list(map(int, sys.stdin.readline().rstrip().split()))

print('%d %d' %(min(inputDataList), max(inputDataList)))