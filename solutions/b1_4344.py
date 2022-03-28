'''
Link        : https://www.acmicpc.net/problem/4344
Difficulty  : BRONZE-1
Category    : 수학, 사칙연산
Title       : 평균은 넘겠지
'''

import sys

c = int(sys.stdin.readline().rstrip())
inputDataList = list()
for i in range(c):
    inputDataList.append(list(map(int, sys.stdin.readline().rstrip().split())))

for data in inputDataList:
    average = (sum(data) - data[0]) / data[0]
    cnt = 0
    for i in range(len(data)):
        if(i == 0):
            continue
        if(data[i] > average):
            cnt += 1
    
    print('%0.3f%%' %(cnt / data[0] * 100))