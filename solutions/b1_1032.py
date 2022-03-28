'''
Link        : https://www.acmicpc.net/problem/1032
Difficulty  : BRONZE-1
Category    : 구현, 문자열
Title       : 명령 프롬프트
'''

n = int(input())
a = list(input())
a_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))