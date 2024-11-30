# 그리디 알고리즘은 최적해를 구하는 아이디어와 경우의 수를 고정시키는 방법도 생각해야 함

import sys
input = sys.stdin.readline

n = int(input())
start = list(map(int,input().strip()))
target = list(map(int,input().strip()))

def change(A,B):
    A_copy = A.copy()
    cnt = 0

    for i in range(1,n):
        
        if A_copy[i-1] == B[i-1]:
            continue
        
        for j in range(i-1,i+2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]
        
        cnt += 1
    
    if A_copy == B:
        return cnt
    else:
        return 1e9
    
# 첫번째 스위치를 안 눌렀을 때
ans = change(start, target)
# 첫번째 스위치를 눌렀을 때
start[0] = 1 - start[0]
start[1] = 1 - start[1]
ans2 = change(start, target)

answer = min(ans, ans2+1)

if answer != 1e9:
    print(answer)
else:
    print(-1)