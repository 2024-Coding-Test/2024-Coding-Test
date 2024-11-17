# 시작 노드에서 가장 멀리 있는 노드(= 가장 끝에 있는 노드)를 구함 
# 해당 노드에서 가장 멀리 있는 노드까지의 거리를 구함

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

visited = [0] * (N+1)
def dfs(current, parent, visited):
    for b,c in tree[current]:
        if b != parent:
            visited[b] = visited[current] + c
            dfs(b,current,visited)

dfs(1,0,visited)
end_node = visited.index(max(visited))

visited = [0] * (N+1)
dfs(end_node,0,visited)
print(max(visited))