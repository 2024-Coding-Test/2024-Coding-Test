import sys
input = sys.stdin.readline

r,c = map(int,input().split())
alphabet = [list(input().strip()) for _ in range(r)]

visited = set()
visited.add(alphabet[0][0])
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alphabet[nx][ny] not in visited:
            visited.add(alphabet[nx][ny])
            dfs(nx,ny,count+1)
            visited.remove(alphabet[nx][ny]) # 백트래킹 알고리즘의 핵심, 바로 직전 상태로 되돌려서 다른 경로를 탐색

dfs(0,0,1)
print(answer)