# 최소힙
# 1. 배열에 자연수 X를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

# heapq 라이브러리 사용
from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            a = heapq.heappop(heap)
            print(a)

    if x > 0:
        heapq.heappush(heap, x)

# Priority Queue 라이브러리 사용
from queue import PriorityQueue
from sys import stdin

q = PriorityQueue()
N = int(stdin.readline())
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if q.qsize() == 0:
            print(0)
        else:
            a = q.get()
            print(a)
    if x > 0:
        q.put(x)

# 직접 구현
from sys import stdin

class MinHeap:
    def __init__(self):
        self.heap = []

    # 부모 노드 인덱스 계산
    def parent(self, i):
        return (i - 1) // 2

    # 왼쪽 자식 노드 인덱스 계산
    def left_child(self, i):
        return 2 * i + 1

    # 오른쪽 자식 노드 인덱스 계산
    def right_child(self, i):
        return 2 * i + 2

    # 두 노드 위치 교환
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 데이터 추가
    def insert(self, x):
        self.heap.append(x) # 새로운 데이터 마지막에 추가
        self._heapify_up(len(self.heap)-1) # 추가된 데이터 재정렬

    def _heapify_up(self, i):
        parent = self.parent(i) # i의 부모 찾기

        # 현재 노드 루트 아니고, 부모보다 작으면 위치 교환
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent) # 재귀

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        # 왼쪽 자식이 현재 노드보다 작으면 min_index 갱신
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        # 오른쪽 자식이 현재 노드보다 작으면 min_index 갱신
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        # 현재 노드가 자식 노드보다 크면 교환하고 재귀 호출
        if i != min_index:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return 0
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

N = int(stdin.readline())
heap = MinHeap()

for _ in range(N):
    x = int(stdin.readline())

    if x > 0:
        heap.insert(x)
    if x == 0:
        print(heap.extract_min())
