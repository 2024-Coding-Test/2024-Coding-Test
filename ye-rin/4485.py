import heapq

# 상하좌우 이동을 위한 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, cave):
    INF = int(1e9)
    # 최소 비용 저장용 배열
    distance = [[INF] * n for _ in range(n)]
    # 시작점 (0, 0)의 비용을 초기화
    distance[0][0] = cave[0][0]
    
    # 우선순위 큐를 사용하여 다익스트라 알고리즘 구현
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))  # (비용, x좌표, y좌표)

    while q:
        dist, x, y = heapq.heappop(q)

        # 현재 꺼낸 경로가 이미 처리된 경로보다 비용이 크다면 무시
        if dist > distance[x][y]:
            continue

        # 현재 노드와 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + cave[nx][ny]

                # 더 적은 비용으로 갈 수 있다면 갱신
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    # 목표 지점 (n-1, n-1)까지의 최소 비용 반환
    return distance[n-1][n-1]

index = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    cave = []
    for _ in range(n):
        cave.append(list(map(int, input().split())))
    
    result = dijkstra(n, cave)
    
    print(f"Problem {index}: {result}")
    index += 1