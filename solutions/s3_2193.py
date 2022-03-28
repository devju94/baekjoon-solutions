'''
Link        : https://www.acmicpc.net/problem/2193
Difficulty  : SILVER-3
Category    : 다이나믹 프로그래밍
Title       : 이친수
'''

import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(91)]
dp[1] = 1
dp[2] = 1
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])