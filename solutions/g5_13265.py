'''
Link        : https://www.acmicpc.net/problem/13265
Difficulty  : GOLD-5
Category    : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
Title       : 색칠하기
'''

import sys

T = int(input())
output = ''
for tc in range(T):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for i in range(m):
        n1, n2 = map(int, sys.stdin.readline().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    chk = [0] * (n+1)
    
    for number in range(1, n+1):
        if not chk[number]:

            stack = [[number, 1]]
            result = 'possible'

            while stack:
                cn, nc = stack.pop()
                if chk[cn] and chk[cn] != nc:
                    result = 'impossible'
                    break
                chk[cn] = nc

                for nn in adj[cn]:
                    if not chk[nn]:
                        stack.append([nn, -nc])

            if result == 'impossible':
                output += result + '\n'
                break

    if result == 'possible':
        output += result + '\n'
print(output)