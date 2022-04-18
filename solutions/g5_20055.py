'''
Link        : https://www.acmicpc.net/problem/20055
Difficulty  : GOLD-5
Category    : 구현, 시뮬레이션
Title       : 컨베이어 벨트 위의 로봇
'''

import sys
from collections import deque

# 데이터 입력
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 초기값 설정
robotLocation = deque([0] * N)
topBelt = deque(A[:N])
bottomBelt = deque(reversed(A[N:]))
step = 1

# 루프 시작
while(True):
    # 벨트 회전
    bottomBelt.append(topBelt.pop())
    topBelt.appendleft(bottomBelt.popleft())
    robotLocation.appendleft(0)
    robotLocation.pop()
    
    # 내리는 위치의 로봇을 내림
    if(robotLocation[-1] == 1):
        robotLocation[-1] = 0
    
    # 로봇 이동
    for i in range(N-2, 0, -1):
        # 현재 칸에 로봇이 없거나 다음칸에 로봇이 있거나 다음칸 내구도가 0이면 > continue
        if(robotLocation[i] == 0 or robotLocation[i+1] == 1 or topBelt[i+1] == 0):
            continue
        else:
            # 로봇 전진
            robotLocation[i] = 0
            robotLocation[i+1] = 1
            # 내구도 감소
            topBelt[i+1] -= 1
            
            # 내리는 위치의 로봇을 내림
            if(i == N-2 and robotLocation[-1] == 1):
                robotLocation[-1] = 0
    
    # 올리는 위치의 내구도가 0보다 크면 로봇을 올린다.
    if(topBelt[0] > 0):
        robotLocation[0] = 1
        # 내구도 감소
        topBelt[0] -= 1
    
    # 종료 조건
    if(topBelt.count(0) + bottomBelt.count(0) >= K):
        break
    
    step += 1
    
print(step)