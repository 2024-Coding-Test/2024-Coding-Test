# 전력망을 둘로 나누기
# 현재 코드
def dfs(graph, v, visited):
    visited[v] = True
    count = 1
    for i in graph[v]:
        if not visited[i]:
            count += dfs(graph, i, visited)
    return count


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        visited = [False] * (n + 1)
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        count = dfs(graph, 1, visited)
        diff = abs(count - (n - count))

        answer = min(answer, diff)

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer