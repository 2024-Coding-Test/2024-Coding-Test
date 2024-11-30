import sys, heapq
input = sys.stdin.readline

n,d = map(int,input().split())

graph = [[] for _ in range(d+1)]
dist = [1e9] * (d+1)

# d까지의 각 거리를 노드로 생각
# i : 시작 노드 / (도착 노드, 거리)
for i in range(d):
    graph[i].append((i+1, 1))

# start에서 end까지의 거리를 추가
for _ in range(n):
    start, end, length = map(int,input().split())
    if end <= d:
        graph[start].append((end, length))

# 우선순위 큐 사용
q = []
heapq.heappush(q, (0,0)) # q에 (거리, 노드)를 추가
dist[0] = 0 # 0에서 0으로 가는 거리는 0

while q:
    _, node = heapq.heappop(q) 

    # 인접 노드들 확인
    for near_node, weight in graph[node]:
        cost = dist[node] + weight # 노드까지 가는 거리 + 노드에서 인접 노드까지의 거리
        if dist[near_node] > cost: # 기존 거리보다 가까워지면 업데이트
            dist[near_node] = cost
            heapq.heappush(q, (cost, near_node)) # 업데이트 될 때만 우선 순위 큐에 추가

print(dist[d])