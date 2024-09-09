from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배로 확대하여 대각선 이동 방지
    def scale_up(coord):
        return [2*x for x in coord]
    
    # 직사각형, 캐릭터, 아이템 좌표 2배 확대
    rectangle = [scale_up(r) for r in rectangle]
    characterX, characterY = scale_up([characterX, characterY])
    itemX, itemY = scale_up([itemX, itemY])
    
    # 지도 크기 정의 (최대 좌표 50, 2배 확대로 100, 여유 1)
    SIZE = 101
    
    # 지도 초기화 (0: 이동 불가, 1: 이동 가능)
    map_data = [[0] * SIZE for _ in range(SIZE)]
    
    # 직사각형 테두리를 지도에 표시
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            map_data[y1][x] = 1
            map_data[y2][x] = 1
        for y in range(y1, y2 + 1):
            map_data[y][x1] = 1
            map_data[y][x2] = 1
    
    # 직사각형 내부 제거
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                map_data[y][x] = 0
    
    # BFS를 위한 큐 초기화
    queue = deque([(characterX, characterY, 0)])  # (x, y, distance)
    visited = set([(characterX, characterY)])
    
    # 이동 방향 정의 (상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    # BFS 실행
    while queue:
        x, y, distance = queue.popleft()
        
        # 목표 지점에 도달한 경우
        if (x, y) == (itemX, itemY):
            return distance // 2  # 2배로 확대했으므로 2로 나눔
        
        # 네 방향으로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 새 위치가 유효하고 방문하지 않았으며 이동 가능한 경우
            if 0 <= nx < SIZE and 0 <= ny < SIZE and map_data[ny][nx] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, distance + 1))
                visited.add((nx, ny))
    
    # 경로를 찾지 못한 경우
    return -1