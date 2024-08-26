import heapq

n,k = map(int,input().split())
distance = [1e9] * 100001 # 최단 거리 테이블

def dijkstra(start):
    distance[start] = 0 # 출발 노드를 선택하고 거리를 0으로 초기화
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 큐에서 추출한 거리가 이미 갱신된 거리보다 클 경우는 방문한 노드이기 때문에 무시
            continue
        for n in (now+1, now-1, now*2): # 인접 노드 확인
            if n < 0 or n > 100000:
                continue
                
            cost = dist
            if n != now*2:
                cost = dist + 1
            
            if cost < distance[n]:
                distance[n] = cost # 최단 거리 테이블 업데이트
                q.append((cost, n))

dijkstra(n)
print(distance[k])