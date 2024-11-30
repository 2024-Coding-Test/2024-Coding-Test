from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
map = [list(map(int,input().strip())) for _ in range(N)]
# visited[x][y][0] : 벽을 부수지 않은 경로, visited[x][y][1] : 벽을 부순 경로
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a,b,c = queue.popleft()
        if a == N-1 and b == M-1:
            return visited[a][b][c]
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 다음 이동할 곳이 벽이고, 벽을 파괴할 기회가 있는 경우
            if map[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx,ny,1))
            # 다음 이동할 곳이 벽이 아니고, 아직 방문하지 않은 곳일 경우
            elif map[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx,ny,c))
    
    return -1

print(bfs(0,0,0))