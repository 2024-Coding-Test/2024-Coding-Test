import sys, heapq
input = sys.stdin.readline

# N : 학생 수, M : 도로 개수, X : 파티 하는 마을
N, M, X = map(int,input().split())
graph = [[] for _ in range(M+1)]
for _ in range(M):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))

def dijkstra(start):

    distance = [1e9] * (M+1)
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드 정보 삽입
    distance[start] = 0 # 자기 자신까지의 거리는 0
    while q:
        dist, node = heapq.heappop(q)
        # 만약 큐에서 추출한 거리가 갱신되어 있는 거리보다 멀다면 무시 (= 이미 방문 했다는 의미)
        if distance[node] < dist:
            continue
        # 큐에서 추출한 노드와 인접한 노드 탐색
        for next in graph[node]:
            cost = distance[node] + next[1] # (시작 노드 -> 노드) + (노드 -> 인접 노드)
            if cost < distance[next[0]]: # cost가 갱신되어 있는 거리보다 가까운 경우에 업데이트
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance


answer = 0
# 각 학생 별 최단 거리 계산
# 파티 마을로 가는 거리 + 파티 마을에서 오는 거리
for i in range(1,N+1):
    distance = dijkstra(i)
    tmp = distance[X]
    distance = dijkstra(X)
    tmp += distance[i]
    answer = max(answer,tmp)

print(answer)