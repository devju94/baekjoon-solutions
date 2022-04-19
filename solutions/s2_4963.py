'''
Link        : https://www.acmicpc.net/problem/4963
Difficulty  : SILVER-2
Category    : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
Title       : 섬의 개수
'''

import sys
from collections import deque
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(mapData, w, h):
    visited = [[0]*w for _ in range(h)]
    islandCnt = 0
    for i in range(h):
        for j in range(w):
            if(mapData[i][j] == 1 and visited[i][j] == 0):
                islandCnt += 1
                queue = deque([(i,j)])
                visited[i][j] = 1
                while(queue):
                    n = queue.popleft()
                    for d in range(8):
                        nr = n[0] + dr[d]
                        nc = n[1] + dc[d]
                        if(nr >= 0 and nc >= 0 and nr <= h-1 and nc <= w-1):
                            if(mapData[nr][nc] == 1 and visited[nr][nc] == 0):
                                queue.append((nr,nc))
                                visited[nr][nc] = 1
    return islandCnt

while(True):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if(w == 0 and h == 0):
        break
    mapData = list()
    for i in range(h):
        mapData.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    visited = [[0 for _ in range(w)] for _ in range(h)]
    print(bfs(mapData, w, h))