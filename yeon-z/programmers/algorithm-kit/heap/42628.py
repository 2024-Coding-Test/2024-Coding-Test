# 우선순위 큐
# 현재 코드
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(min_heap, int(i[1:]))
            heapq.heappush(max_heap, (-int(i[1:]), int(i[1:])))
        elif len(min_heap) == 0:
            continue
        elif int(i[1:]) == 1:
            heapq.heappop(max_heap)
            min_heap.pop()
        else:
            heapq.heappop(min_heap)
            max_heap.pop()
    if len(min_heap) > 0:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]