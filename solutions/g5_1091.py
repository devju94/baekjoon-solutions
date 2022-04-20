'''
Link        : https://www.acmicpc.net/problem/1091
Difficulty  : GOLD-5
Category    : 구현, 시뮬레이션
Title       : 카드 섞기
'''

import sys
from copy import deepcopy

# 데이터 입력
N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
S = list(map(int, sys.stdin.readline().rstrip().split()))

# 초기값 설정
suffle_count = 0
card_list_origin = list(range(N))
card_list_temp = list(range(N))
card_list_suffled = list(range(N))

while(True):
    # 섞은 카드로 card_list 갱신
    card_list_temp = deepcopy(card_list_suffled)
    
    # 현재 카드 리스트가 목적을 달성하는지 확인
    check = True
    for i in range(N):
        target = i % 3
        if(target != P[card_list_suffled[i]]):
            check = False
            break
    
    # 목적 달성했으면 종료
    if(check == True):
        print(suffle_count)
        break
    
    # 카드 섞기
    for i in range(N):
        card_list_suffled[S[i]] = card_list_temp[i]
    suffle_count += 1
    
    # 목적 달성 불가능
    if(card_list_suffled == card_list_origin):
        print(-1)
        break