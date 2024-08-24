# 숨바꼭질 3
# 수빈이는 현재 점N(0 <= N <= 100000)에 있고,
# 동생은 점K(0 <= K <= 100000)에 있다.
# 수빈이는 걷거나 순간이동 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구해

from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().strip().split())
limit = 100001
time = [limit] * limit
visited = [False] * limit

def bfs(x, y):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        visited[x] = True

        if x == y:
            return time[x]

        for nx in (x+1, x-1, x*2):
            # print(nx, time[:K+1])
            if 0 <= nx < limit and not visited[nx]:
                if nx == x * 2:
                    time[nx] = min(time[x], time[nx])
                    q.appendleft(nx)
                else:
                    time[nx] = min(time[x] + 1, time[nx])
                    q.append(nx)

    return q[y]
time[N] = 0
print(bfs(N, K))

