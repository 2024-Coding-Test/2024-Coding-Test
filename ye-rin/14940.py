from collections import deque

def bfs_shortest_path(grid, start):
    n, m = len(grid), len(grid[0])  # 지도(격자)의 행과 열의 크기
    distances = [[-1] * m for _ in range(n)]  # 각 지점까지의 최단 거리를 저장할 2차원 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 네 방향으로 이동

    queue = deque([start])  # BFS 탐색을 위한 큐 초기화, 시작점을 큐에 추가
    distances[start[0]][start[1]] = 0  # 시작점의 거리를 0으로 초기화 (자기 자신까지의 거리는 0)

    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냄

        for dx, dy in directions:  # direction-x, direction-y
            nx, ny = x + dx, y + dy  # 현재 위치 (x, y)에서 새로운 위치 (nx, ny)를 계산

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                # 새 위치가 격자 범위 내에 있고, 이동 가능하며, 아직 방문하지 않은 경우
                distances[nx][ny] = distances[x][y] + 1  # 새 위치의 거리를 현재 위치의 거리 +1로 설정
                queue.append((nx, ny))  # 새 위치를 큐에 추가하여, 이 위치에서 다시 주변을 탐색하도록 큐에 넣음

    return distances  # 모든 위치까지의 최단 거리가 저장된 2차원 리스트를 반환

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 목표 지점 찾기
start = None
for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            start = (i, j)
            break
    if start:   # 외부 루프도 종료하기 위해 사용
        break

distances = bfs_shortest_path(grid, start)

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()