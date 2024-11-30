import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
plan = list(map(int,input().split()))
visited = [False] * n

#BFS 풀이
# from collections import deque

# def bfs(n):
#     q = deque()
#     q.append(n)
#     visited[n] = True

#     while q:
#         now = q.popleft()
#         for idx, connect in enumerate(graph[now]):
#             if connect and not visited[idx]:
#                 visited[idx] = True
#                 q.append(idx)

# bfs(plan[0]-1)

# can = True
# for p in plan:
#     if not visited[p-1]:
#         can = False

# if can:
#     print('YES')
# else:
#     print('NO')

# 유니온-파인드 풀이
# 부모 노드가 같다면 노드들이 연결되어 있음
def find_parent(parent, x): # 부모 노드를 찾는 함수
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # a 노드와 b 노드의 부모 노드를 합치는 함수
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [k for k in range(n+1)]
for i in range(n):
    for idx, j in enumerate(graph[i]):
        if j == 1:
            union_parent(parent, i, idx)

cycle = True
for idx,city in enumerate(plan[:-1]):
    # 현재 탐색하는 노드와 다음에 탐색할 노드의 부모 노드가 다르다면, 두 노드의 사이클은 다른 사이클
    if find_parent(parent, city-1) != find_parent(parent, plan[idx+1]-1): 
        cycle = False
        break

if cycle == True:
    print("YES")
else:
    print("NO")