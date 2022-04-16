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

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

data[r][c] = 2
cleanCnt = 1
while(True):
    stopFlag = True
    
    for i in range(4):
        nextD = (d+3-i)%4
        nextR = r + dr[nextD]
        nextC = c + dc[nextD]
        
        if(data[nextR][nextC] == 0):
            d = nextD
            r = nextR
            c = nextC
            data[r][c] = 2
            cleanCnt += 1
            stopFlag = False
            break

    if(stopFlag == False):
        continue
    
    # 후진
    r += dr[(d+2)%4]
    c += dc[(d+2)%4]
    
    # 현재 위치가 벽이면 종료
    if(data[r][c] == 1):
        break

print(cleanCnt)