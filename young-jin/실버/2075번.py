import heapq

n = int(input())
heap = []

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # n개의 노드 중에 가장 작은 노드 = n번째로 큰 노드
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap,number)

print(heap[0])