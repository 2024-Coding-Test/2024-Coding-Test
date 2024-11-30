import sys, heapq
input = sys.stdin.readline

num = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        rupee = [list(map(int,input().split())) for _ in range(N)]
        distance = [[int(1e9)] * N for _ in range(N)]

        # start = [0,0]
        def dijkstra(start):
            # 상하좌우 이동
            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            q = []
            heapq.heappush(q, (0, start))
            i,j = start
            distance[i][j] = rupee[i][j]

            while q:
                dist, node = heapq.heappop(q)
                i,j = node
                if distance[i][j] < dist:
                    continue
                for z in range(4):
                    if 0 <= i+dy[z] <= N-1 and 0 <= j+dx[z] <= N-1:
                        x = j+dx[z]; y = i+dy[z]
                        cost = distance[i][j] + rupee[y][x]
                        if cost < distance[y][x]:
                            distance[y][x] = cost
                            heapq.heappush(q, (cost, [y, x]))

        dijkstra([0,0])

        ans = distance[N-1][N-1]

        print(f"Problem {num}: {ans}")
        num += 1