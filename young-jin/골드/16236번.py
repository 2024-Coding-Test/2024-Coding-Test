from collections import deque

N = int(input())
space = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos = [i,j]

def bfs(x,y):
    visited = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append([x,y])
    cand = []
    visited[x][y] = 1

    while queue:
        i,j = queue.popleft()
        for idx in range(4):
            ii,jj = i + dx[idx], j + dy[idx]
            
            if 0 <= ii < N and 0 <= jj < N and visited[ii][jj] == 0:
                # 물고기를 먹을 수 있는 경우 후보군에 저장
                if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj]-1, ii, jj))
                elif space[x][y] == space[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii,jj])
                elif space[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append([ii,jj])
    
    return sorted(cand, key = lambda x : (x[0],x[1],x[2]))

i,j = pos
size = [2,0]
cnt = 0
while True:
    space[i][j] = size[0]
    cand = deque(bfs(i,j))

    # 먹을 수 있는 물고기가 없어질 때까지 반복
    if not cand:
        break
    
    # 후보군을 하나씩 추출
    step,xx,yy = cand.popleft()
    cnt += step
    # 지금까지 몇 마리를 먹었는지 확인
    size[1] += 1

    # 지금 아기 상어의 크기와 먹은 물고기 수가 같으면
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    
    # 물고기를 먹은 지점부터 다시 bfs를 하기 위해 기존 시작 지점을 0(빈칸)으로 설정
    # 현재 위치를 물고기를 먹은 지점으로 설정
    space[i][j] = 0
    i,j = xx,yy

print(cnt)