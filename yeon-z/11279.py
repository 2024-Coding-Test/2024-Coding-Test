# 최대 힙
from sys import stdin
import heapq

N = int(stdin.readline())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0 and len(heap) > 0:
        print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, -x)