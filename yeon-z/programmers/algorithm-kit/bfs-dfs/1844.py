# 게임 맵 최단거리
# 현재 코드
from collections import deque


def solution(maps):
    # 상 하 좌 우
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    answer = 0

    n = len(maps[0])
    m = len(maps)

    visited = [[-1] * n for _ in range(m)]
    visited[0][0] = 1

    # 도착지점에 갈 수 없는 경우
    if maps[m - 2][n - 1] == 0 and maps[m - 1][n - 2] == 0:
        return -1

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for d in directions:
            dx, dy = x + d[0], y + d[1]
            if 0 <= dx < m and 0 <= dy < n and visited[dx][dy] == -1 and maps[dx][dy] == 1:
                queue.append((dx, dy))
                visited[dx][dy] = visited[x][y] + 1

    return visited[m - 1][n - 1]

# 이전 코드
from collections import deque
def solution(maps):
    n = len(maps) # 세로
    m = len(maps[0]) # 가로

    start = (0, 0)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < m) and visited[nx][ny] == -1 and maps[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[n-1][m-1]