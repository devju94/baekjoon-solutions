'''
Link        : https://www.acmicpc.net/problem/14503
Difficulty  : GOLD-5
Category    : 구현, 시뮬레이션
Title       : 로봇 청소기
'''

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())

data = list()
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

cleaned = set()
cleaned.add((r,c))
stopFlag = 0
cleanCnt = 1
while(True):
    # 현재 위치의 왼쪽 방향(nextD), 좌표(nextPos) 계산
    if(d == 0):
        nextD = 3
        nextPos = (r, c-1)
    elif(d == 1):
        nextD = 0
        nextPos = (r-1, c)
    elif(d == 2):
        nextD = 1
        nextPos = (r, c+1)
    elif(d == 3):
        nextD = 2
        nextPos = (r+1, c)
    
    # 해당 칸이 청소하지 않은 빈공간인지 확인
    if(data[nextPos[0]][nextPos[1]] == 0 and nextPos not in cleaned):
        # 방향 왼쪽으로 전환 후, 청소
        stopFlag = 0
        cleanCnt += 1
        cleaned.add(nextPos)
        r = nextPos[0]
        c = nextPos[1]
        d = nextD
    else:
        # 방향만 왼쪽으로 전환
        stopFlag += 1
        d = nextD
    
    # 현재 위치의 뒷쪽 칸 좌표(backPos) 계산
    if(d == 0): backPos = (r+1, c)
    elif(d == 1): backPos = (r, c-1)
    elif(d == 2): backPos = (r-1, c)
    elif(d == 3): backPos = (r, c+1)
    # 작동 정지 조건
    if(stopFlag == 4):
        if(data[backPos[0]][backPos[1]] == 1):
            # 작동 정지
            break
        else:
            # 후진
            stopFlag = 0
            r = backPos[0]
            c = backPos[1]

print(cleanCnt)