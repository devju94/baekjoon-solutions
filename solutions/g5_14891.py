'''
Link        : https://www.acmicpc.net/problem/14891
Difficulty  : GOLD-5
Category    : 구현, 시뮬레이션
Title       : 톱니바퀴
'''

import sys
from collections import deque


# 데이터 입력
gearStatusList = list()
for i in range(4):
    gearStatusList.append(deque(list(sys.stdin.readline().rstrip())))

K = int(sys.stdin.readline().rstrip())
rotateDataList = list()
for i in range(K):
    rotateDataList.append(list(map(int, sys.stdin.readline().rstrip().split())))


# 톱니바퀴 회전 함수
def rotate(gearStatus, direction):
    if(direction == 1): # 시계 방향
        temp = gearStatus.pop()
        gearStatus.appendleft(temp)
    else: # 반시계 방향
        temp = gearStatus.popleft()
        gearStatus.append(temp)

    return gearStatus
    
    
# 톱니바퀴 회전 실행
for i in range(K):
    target = rotateDataList[i][0] - 1
    
    newGearStatusList = list(gearStatusList)
    newGearStatusList[target] = rotate(deque(gearStatusList[target]), rotateDataList[i][1])
    
    # 좌측으로 인접한 톱니바퀴 회전
    if(target > 0):
        for j in range(target-1, -1, -1):
            if(gearStatusList[j+1][6] != gearStatusList[j][2]):
                # 회전 방향 계산
                if((target - j) % 2 == 0):
                    direction = rotateDataList[i][1]
                else:
                    direction = rotateDataList[i][1] * -1
                # 회전
                newGearStatusList[j] = rotate(deque(gearStatusList[j]), direction)
            else:
                # 회전하지 않음
                break
    
    # 우측으로 인접한 톱니바퀴 회전
    if(target < 3):
        for k in range(target+1, 4):
            if(gearStatusList[k-1][2] != gearStatusList[k][6]):
                # 회전 방향 계산
                if((k - target) % 2 == 0):
                    direction = rotateDataList[i][1]
                else:
                    direction = rotateDataList[i][1] * -1
                # 회전
                newGearStatusList[k] = rotate(deque(gearStatusList[k]), direction)
            else:
                # 회전하지 않음
                break
    
    # 톱니바퀴 상태 갱신
    gearStatusList = list(newGearStatusList)


# 점수 합 계산
result = 0
for i in range(4):
    if(newGearStatusList[i][0] == '1'):
        result += (2 ** i)


# 점수 합 출력
print(result)