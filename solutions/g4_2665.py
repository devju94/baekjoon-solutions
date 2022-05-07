'''
Link        : https://www.acmicpc.net/problem/2665
Difficulty  : GOLD-4
Category    : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 다익스트라
Title       : 미로만들기
'''

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
    
def bfs():
    queue = deque([[0, 0]])
    visited[0][0] = 0
    
    while(queue):
        curr_r, curr_c = queue.popleft()
        
        if(curr_r == n-1 and curr_c == n-1):
            return visited[curr_r][curr_c]

        for i in range(4):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]
            if(next_r >= 0 and next_r < n and next_c >= 0 and next_c < n and visited[next_r][next_c] == -1):
                # 검은방
                if(data[next_r][next_c] == 0):
                    visited[next_r][next_c] = visited[curr_r][curr_c] + 1
                    queue.append([next_r, next_c])
                # 방문하지 않은 흰방
                else:
                    visited[next_r][next_c] = visited[curr_r][curr_c]
                    queue.appendleft([next_r, next_c])
        
# 데이터 입력
n = int(sys.stdin.readline().rstrip())
data = list()
for __ in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [[-1]*n for __ in range(n)]
print(bfs())