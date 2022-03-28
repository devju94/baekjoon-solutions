'''
Link        : https://www.acmicpc.net/problem/11441
Difficulty  : SILVER-3
Category    : 누적합
Title       : 합 구하기
'''

import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())

prefixSum = [0] * (N+1)
for i in range(1, len(A)+1):
    prefixSum[i] = prefixSum[i-1] + A[i-1]

for x in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefixSum[j]-prefixSum[i-1])