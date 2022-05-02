'''
Link        : https://www.acmicpc.net/problem/2206
Difficulty  : GOLD-4
Category    : 그래프 이론, 그래프 탐색, 너비 우선 탐색
Title       : 벽 부수고 이동하기
'''

import sys
from collections import deque

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(visited, map_data):
    queue = deque([[0, 0, 0]])
    visited[0][0][0] = 1
    while(queue):
        curr_r, curr_c, used_break_wall = queue.popleft()
        
        # 끝점이면 종료
        if(curr_r == N-1 and curr_c == M-1):
            return visited[curr_r][curr_c][used_break_wall]
        
        # 사방 탐색
        for i in range(4):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]
            if(next_r < 0 or next_r > N-1 or next_c < 0 or next_c > M-1):
                continue
            
            # 벽
            if(map_data[next_r][next_c] == 1):
                if(used_break_wall == 1):
                    continue
                else:
                    visited[next_r][next_c][1] = visited[curr_r][curr_c][0] + 1
                    queue.append([next_r, next_c, 1])
            
            # 벽이 아닌 방문하지 않은 칸
            elif(visited[next_r][next_c][used_break_wall] == 0):
                visited[next_r][next_c][used_break_wall] = visited[curr_r][curr_c][used_break_wall] + 1
                queue.append([next_r, next_c, used_break_wall])
    
    # 불가능
    return -1

# 데이터 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
map_data = list()
for i in range(N):
    map_data.append(list(map(int, sys.stdin.readline().rstrip())))

# bfs 실행
visited = [[[0] * 2 for __ in range(M)] for __ in range(N)]
result = bfs(visited, map_data)
print(result)