from collections import deque

def solution(n, edge):
    answer = {num : 0 for num in range(1,n+1)}
    graph = {num : [] for num in range(1,n+1)}
    
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    
    def bfs(g,start,visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            for i in g[v]:
                if not visited[i]:
                    answer[i] += 1 + answer[v]
                    visited[i] = True
                    queue.append(i)
    
    visited = [False] * (n+1)
    
    bfs(graph, 1, visited)

    m = max(answer.values())

    count = 0
    for i in answer.values():
        if i == m:
            count += 1

    return count