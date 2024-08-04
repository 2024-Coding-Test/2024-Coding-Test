from sys import stdin as s 
import math
# s = open("input.txt", "rt")

N, X = map(int, s.readline().strip().split())
cnt = list(map(int, s.readline().strip().split()))

# # 시간초과
# for i in range(len(cnt)-X+1):
    # result.append(sum(cnt[i:i+X]))
    
# 슬라이딩 윈도우 알고리즘을 사용해서 시간초과 해결
window = sum(cnt[:X])
result = [window]

for i in range(X, N):
    window += cnt[i] - cnt[i-X]
    result.append(window)

if max(result) == 0:
    print("SAD")
else:
    res = max(result)
    print(res)
    print(result.count(res))