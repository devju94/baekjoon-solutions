'''
Link        : https://www.acmicpc.net/problem/9519
Difficulty  : SILVER-1
Category    : 수학, 구현, 문자열, 시뮬레이션
Title       : 졸려
'''

import sys
from collections import deque


def closeEye(word):
    frontQ = deque()
    backQ = deque()
    newWord = ''
    
    # 홀수인덱스는 그대로, 짝수인덱스는 역순으로 큐에 삽입
    for i in range(len(word)):
        if(i % 2 == 0):
            frontQ.append(word[i])
        else:
            backQ.appendleft(word[i])

    # front, back 순으로 모두 popleft하여 이어붙이기
    while(frontQ):
        newWord += frontQ.popleft()
    while(backQ):
        newWord += backQ.popleft()
    
    return newWord


def solution(X, word):
    # cnt(원래대로 돌아오는 반복 횟수) 값 계산
    cnt = 1
    tempWord = closeEye(word)
    while(tempWord != word):
        tempWord = closeEye(tempWord)
        cnt += 1
    
    # X값을 cnt로 나눈 나머지로 조정
    X %= cnt 
    
    # X가 0이면 그대로 반환
    if(X == 0):
        return word
    
    # X만큼 반복
    for i in range(X):
        word = closeEye(word)
    
    return word

X = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
print(solution(X, word))