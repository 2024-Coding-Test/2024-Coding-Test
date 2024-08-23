# DFS 출 BFS 출력
from sys import stdin
from collections import deque

# N 정점 수
# M 간선 수
# V 시작 번호
N, M, V = map(int, stdin.readline().strip().split())

vertex = {}

for i in range(1, N+1):
    vertex[i] = []

for _ in range(M):
    v1, v2 = map(int, stdin.readline().strip().split())
    vertex[v1].append(v2)
    vertex[v2].append(v1)

def BFS(startVertex):
    # 넓이 우선
    visited = []
    queue = deque([startVertex])

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            queue.extend(vertex[current])
    for idx, v in enumerate(visited):
        if idx == len(visited)-1:
            print(v, end='\n')
        else:
            print(v, end=' ')
def DFS(startVertex):
    # 깊이 우선
    visited = []
    stack = [startVertex]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(vertex[current])
    for idx, v in enumerate(visited):
        if idx == len(visited)-1:
            print(v, end='\n')
        else:
            print(v, end=' ')

for i in vertex.keys():
    vertex[i].sort(reverse=True)
DFS(V)

for i in vertex.keys():
    vertex[i].sort()
BFS(V)
