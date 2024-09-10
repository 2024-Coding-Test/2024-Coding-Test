from collections import deque
import copy

# 특정 좌표를 본인이 속한 사각형 외의 모든 사각형과 비교하여,
# 하나라도 어떤 사각형의 내부에 위치하는지를 판단해주는 함수
def is_in_square(pos_x, pos_y, rec_num, rectangle):
    for x1, y1, x2, y2 in rectangle[:rec_num] + rectangle[rec_num+1:]:
        if x1 < pos_x < x2 and y1 < pos_y < y2:
            return True
    
    return False

# 인접 노드 제너레이터
def move(x, y):
    if 1 <= x-1 <= 100:
        yield (x-1, y)
    if 1 <= x+1 <= 100:
        yield (x+1, y)
    if 1 <= y-1 <= 100:
        yield (x, y-1)
    if 1 <= y+1 <= 100:
        yield (x, y+1)

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 모든 좌표를 2배 늘려줌
    # 해당 풀이의 핵심은, 다각형 모양의 테두리에 해당하는 좌표를 찾아
    # 모두 1을 넣어두고, 출발지로부터 4방향으로 BFS 탐색해나가면서
    # 값이 1이고 visited가 0인 노드로 계속 뻗어나가는 것인데,
    # ㄷ(디귿) 자 모양의 경우를 생각해보면, 오른쪽 아래에서
    # 오른쪽 위 노드는 값이 1이므로 뻗어나가게 되는데 실제로는
    # 연결된 노드가 아니므로 뻗어나가서는 안된다.
    # 이런 예외적인 경우를 해결하기 위해 좌표를 두 배 늘려줌
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j] *= 2
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    answer = 0
    roadmap = [[0]*101 for _ in range(101)]
    visited = copy.deepcopy(roadmap)
    
    # 모든 사각형을 돌면서, 각 사각형의 모든 좌표를 순회하며
    # 그 것이 본인을 제외한 다른 모든 사각형의 내부에 단 하나도
    # 속하지 않는다면 roadmap에 1로 표기
    # 요약하면 다각형의 테두리 좌표를 싹 다 구하는 구문
    rec_num = 0
    for x1, y1, x2, y2 in rectangle:
        # 사각형의 가로 변의 모든 좌표들을 대상으로
        # 유효한 좌표인지 검사
        for x in range(x1, x2+1):
            if not is_in_square(x, y1, rec_num, rectangle):
                roadmap[x][y1] = 1
            if not is_in_square(x, y2, rec_num, rectangle):
                roadmap[x][y2] = 1
        
        # 사각형의 세로 변의 모든 좌표들을 대상으로
        # 유효한 좌표인지 검사
        for y in range(y1, y2+1):
            if not is_in_square(x1, y, rec_num, rectangle):
                roadmap[x1][y] = 1
            if not is_in_square(x2, y, rec_num, rectangle):
                roadmap[x2][y] = 1
        
        rec_num += 1
    
    dq = deque([(characterX, characterY)])
    visited[characterX][characterY] = 1
    
    while dq:
        now_x, now_y = dq.popleft()
        
        # 현재 좌표가 목표 좌표이면 그 때의 visited 값 반환
        # 좌표를 두배 해줬었으므로 정답도 원래의 두배가 됨
        # 2 나눠서 리턴
        if (now_x, now_y) == (itemX, itemY):
            answer = visited[now_x][now_y] // 2
            break
        
        # 인접 노드로 뻗어나감
        # 인접 좌표가 유효한 좌표(roadmap이 1)이고 방문한 적이 없다면
        # 뻗어나감(큐에 집어넣음)
        for adj_x, adj_y in move(now_x, now_y):
            if roadmap[adj_x][adj_y] and visited[adj_x][adj_y] == 0:
                dq.append((adj_x, adj_y))
                visited[adj_x][adj_y] = visited[now_x][now_y] + 1
    
    return answer