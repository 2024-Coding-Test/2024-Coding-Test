# 절대갑 힙
from sys import stdin
import heapq

N = int(stdin.readline())
h = []

for _ in range(N):
    command = int(stdin.readline())
    if command != 0:
        heapq.heappush(h, (abs(command), command))
        # print(h)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])