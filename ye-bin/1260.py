from sys import stdin as s 
from collections import deque 

def BFS(start):
    queue = deque()
    visited = [0 for _ in range(N+1)]
    
    queue.append(start)
    visited[start] = 1
    
    while len(queue) > 0:
        current = queue[0]
        print(current, end=' ')
        
        for next in edge[current]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)
        queue.popleft()

def DFS(current):
    print(current, end=' ')
    
    for next in edge[current]:
        if visited[next] == 0:
            visited[next] = 1
            DFS(next)

N, M, V = map(int, s.readline().strip().split())
edge = [[] for _ in range(N+1)]

visited = [0 for _ in range(N+1)]
visited[V] = 1

for i in range(M):
    n1, n2 = map(int, s.readline().strip().split())
    
    # 간선 표현
    edge[n1].append(n2)
    edge[n2].append(n1)

for i in range(1, N+1):
    edge[i].sort()
    
DFS(V)
print()
BFS(V)