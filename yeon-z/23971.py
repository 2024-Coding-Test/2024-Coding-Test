# W개씩 H행
# 세로 N칸, 가로 M칸 이상 비우고 앉아야 함.
import math
from sys import stdin

H, W, N, M = map(int, stdin.readline().strip().split(" "))

hc = math.ceil(H / (N+1))
wc = math.ceil(W / (M+1))

print(wc * hc)
