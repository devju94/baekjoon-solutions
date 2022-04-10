'''
Link        : https://www.acmicpc.net/problem/14719
Difficulty  : GOLD-5
Category    : 구현, 시뮬레이션
Title       : 빗물
'''

import sys

H, W = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

water = 0
for i in range(1, W-1):
    # 현재 블록 기준으로 좌우의 최대 높이 계산
    leftMax = max(data[:i])
    rightMax = max(data[i+1:])
    
    # 좌우의 최대높이가 모두 현재 블록 높이보다 크면 빗물양 누적
    if(leftMax > data[i] and rightMax > data[i]):
        small = min(leftMax, rightMax)
        water += (small - data[i])

print(water)