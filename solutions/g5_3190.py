'''
Link        : https://www.acmicpc.net/problem/3190
Difficulty  : GOLD-5
Category    : 구현, 자료 구조, 시뮬레이션, 덱, 큐
Title       : 뱀
'''

import sys
import copy

# 데이터 입력
N = int(sys.stdin.readline().rstrip())

K = int(sys.stdin.readline().rstrip())
applePosList = list()
for i in range(K):
    applePosList.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
L = int(sys.stdin.readline().rstrip())
dirDataList = list()
for i in range(L):
    dirDataList.append(list(sys.stdin.readline().rstrip().split()))

# 초기값 설정
sec = 0
headPos = [1, 1]
tailPos = [1, 1]
bodyPosList = [[1, 1]]
currDir = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 루프 실행
while(True):
    sec += 1
    # 머리 이동
    headPos[0] += dr[currDir]
    headPos[1] += dc[currDir]
    # bodyPosList에 머리 좌표 추가
    bodyPosList.append(copy.deepcopy(headPos))
    
    # 종료 조건1 - 벽 충돌
    if(headPos[0] < 1 or headPos[0] > N or headPos[1] < 1 or headPos[1] > N ):
        break
    # 종료 조건2 - 몸 충돌
    if(headPos in bodyPosList[:-1]):
        break
    
    # 이동한 칸에 사과가 있는지 확인
    if(headPos in applePosList):
        del applePosList[applePosList.index(headPos)]
    else:
        del bodyPosList[0]
        tailPos = copy.deepcopy(bodyPosList[0])

    # 방향 전환
    if(len(dirDataList) > 0):
        if(int(dirDataList[0][0]) == sec):
            dir = dirDataList[0][1]
            if(dir == 'L'):
                currDir = (currDir + 3) % 4
            else:
                currDir = (currDir + 1) % 4
            del dirDataList[0]
            
print(sec)