'''
Link        : https://www.acmicpc.net/problem/2588
Difficulty  : BRONZE-5
Category    : 수학, 사칙연산
Title       : 곱셈
'''

import sys

# 자연수 n을 한 자리 씩 분리한 list 반환
def digitSplit(n):
    result = list()
    while(n > 1):
        result.append(int(n%10))
        n = n/10
    return result

inputDataList = list()
for i in range(2):
    inputDataList.append(int(sys.stdin.readline().rstrip()))

first = inputDataList[0]
second = inputDataList[1]

for i in digitSplit(second):
    print(first*i)

print(first*second)