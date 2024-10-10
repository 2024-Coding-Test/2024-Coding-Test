import heapq

N = int(input())
M = int(input())

network = {}

for i in range(1, N+1):
    network[i] = []

for _ in range(M):
    c1, c2 = map(int, input().split())
    network[c1].append(c2)
    network[c2].append(c1)

def dijkstra(start):
    distance = [int(1e9)] * (N + 1)
    distance[start] = 0
    h = []
    heapq.heappush(h, (distance[start], start))

    while h:
        dist, node = heapq.heappop(h)
        for n in network[node]:
            if dist + 1 < distance[n]:
                distance[n] = dist + 1
                heapq.heappush(h, (distance[n], n))
    cnt  = 0
    for d in distance:
        if d < int(1e9):
            cnt += 1
    return cnt - 1
print(dijkstra(1))