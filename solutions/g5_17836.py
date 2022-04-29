'''
Link        : https://www.acmicpc.net/problem/17836
Difficulty  : GOLD-5
Category    : 그래프 이론, 그래프 탐색, 너비 우선 탐색
Title       : 공주님을 구해라!
'''

import sys
from collections import deque

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 좌표 유효성 확인
def is_valid_pos(r, c):
    if(r >= N or r < 0 or c >= M or c < 0):
        return False
    else:
        return True

# 너비 우선 탐색
def bfs(castle_data, visited):
    min_time_with_sword = 0
    result = 0
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while(queue):
        curr_pos = queue.popleft()
        curr_row = curr_pos[0]
        curr_col = curr_pos[1]
        
        # 공주님 위치 도달
        if(curr_row == N-1 and curr_col == M-1):
            if(min_time_with_sword > 0):
                result = min(min_time_with_sword, visited[curr_row][curr_col])
            else:
                result = visited[curr_row][curr_col]
            
            # 결과 반환
            return result - 1
        
        # '그람' 위치 도달            
        if(castle_data[curr_row][curr_col] == 2):
            min_time_with_sword = visited[curr_row][curr_col] + \
                                (N-1-curr_row) + (M-1-curr_col)
        
        # 사방탐색
        for i in range(4):
            next_row = curr_row + dr[i]
            next_col = curr_col + dc[i]
            
            if(is_valid_pos(next_row, next_col) == False):
                continue
            
            if(visited[next_row][next_col] == 0 and castle_data[next_row][next_col] != 1):
                visited[next_row][next_col] = visited[curr_row][curr_col] + 1
                queue.append((next_row, next_col))
    
    # 공주님 위치에 도달하지 못하고 탐색이 끝났을 경우
    if(min_time_with_sword > 0):
        result = min_time_with_sword
    
    return result - 1


# 데이터 입력
N, M, T = map(int, sys.stdin.readline().rstrip().split())
castle_data = list()
for __ in range(N):
    castle_data.append(list(map(int, sys.stdin.readline().rstrip().split())))

# BFS 실행
visited = [[0]*M for __ in range(N)]
result = bfs(castle_data, visited)

# 결과 출력
if(result > 0 and result <= T):
    print(result)
else:
    print('Fail')