import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())

# 그래프 설정 (출발 노드와 도착 노드)
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 초기화
cow = [1e9] * (n+1)
# 방문 테이블
visited = [False] * (n+1)

# graph[출발노드].append(도착노드, 소의 수)
for _ in range(m):
    ai,bi,ci = map(int,input().split())
    graph[ai].append((bi,ci))
    graph[bi].append((ai,ci))

q = []
heapq.heappush(q, (0,1)) 
cow[1] = 0

while q:
    c, node = heapq.heappop(q)
    if visited[node] == True:
        continue
    else:
        visited[node] = True
    # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 무시
    if cow[node] < c: 
        continue
    # 인접 노드 확인
    for near_node, weight in graph[node]:
        cost = cow[node] + weight
        if cow[near_node] > cost:
            cow[near_node] = cost
            heapq.heappush(q, (cost, near_node))

print(cow[n])