'''
Link        : https://www.acmicpc.net/problem/9625
Difficulty  : SILVER-5
Category    : 구현, 다이나믹 프로그래밍
Title       : BABBA
'''

import sys 

K = int(sys.stdin.readline().rstrip())

a = [1, 0]
b = [0, 1]
 
for i in range(2, K+1):
    a_num = a[i-1] + a[i-2]
    a.append(a_num)
    b_num = b[i-1] + b[i-2]
    b.append(b_num)
 
print(a[K], b[K])