'''
Link        : https://www.acmicpc.net/problem/1065
Difficulty  : SILVER-4
Category    : 브루트포스 알고리즘
Title       : 한수
'''

import sys

def digitSplit(n):
    result = list()
    if(n != 0):
        while(n >= 1):
            result.append(int(n%10))
            n /= 10
    else:
        result.append(0)
        
    return result

# 양의 정수 n이 한수(각 자리가 등차수열을 이루는 수)인지 검사
def isArithmeticSequence(n):
    answer = True
    nToken = digitSplit(n)
    prevNum = 0
    prevDiffer = 0
    differ = 0
    
    # 각 자리가 등차수열을 이루는지 검사
    for i in range(len(nToken)):
        if(i == 0):
            pass
        elif(i == 1):
            prevDiffer = nToken[i] - prevNum
        else:
            differ = nToken[i] - prevNum
            if(differ != prevDiffer):
                answer = False
                break
        
        prevNum = nToken[i]
        
    return answer            

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())

    # 1 이상 T 이하 범위의 한수의 개수 계산
    cnt = 0
    for i in range(1, T+1):
        if(isArithmeticSequence(i) == True):
            cnt += 1

    print(cnt)