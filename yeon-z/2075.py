# N번째 큰수

from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for _ in range(N):
    row = list(map(int, stdin.readline().strip().split()))
    for r in row:
        if len(heap) < N:
            heapq.heappush(heap, r)
        else:
            heapq.heappushpop(heap, r)
print(heap[0])

