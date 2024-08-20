import heapq
import sys

def dijkstra(D, graph):
    # 시작 지점부터 각 위치까지의 최단 거리를 저장하는 리스트, 초기값은 무한대 (float('inf'))로 설정
    dist = [float('inf')] * (D + 1)
    dist[0] = 0  # 시작 지점의 거리는 0으로 설정

    # 우선순위 큐를 사용하여 현재 거리와 현재 위치를 저장
    pq = [(0, 0)]  # (현재 거리, 현재 위치) 형태의 튜플로 저장

    while pq:
        current_dist, current_location = heapq.heappop(pq)  # 큐에서 가장 짧은 거리를 가진 위치를 꺼냄
        
        # 현재 계산된 거리가 기록된 거리보다 크면 무시
        if current_dist > dist[current_location]:
            continue
        
        # 현재 위치에서 이동할 수 있는 모든 경로를 탐색
        for next_location, distance in graph[current_location]:
            new_dist = current_dist + distance  # 새로운 거리를 계산
            if new_dist < dist[next_location]:  # 더 짧은 경로를 발견하면 갱신
                dist[next_location] = new_dist
                heapq.heappush(pq, (new_dist, next_location))  # 큐에 새로운 경로를 추가

    return dist[D]  # 목적지 D까지의 최단 거리를 반환

N, D = map(int, input().split())  # N: 지름길의 개수, D: 고속도로의 길이
graph = [[] for _ in range(D + 1)]  # 각 지점을 노드로 간주하여 그래프를 초기화

# 모든 노드에 대해 기본 도로를 설정
for i in range(D):
    graph[i].append((i + 1, 1))  # 기본적으로 1만큼의 거리를 이동하는 간선을 추가

# 지름길 정보를 입력받아 그래프에 추가
for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D:  # 지름길의 도착점이 고속도로 길이 D를 초과하지 않는 경우에만 추가
        graph[start].append((end, length))

# 다익스트라 알고리즘을 이용해 최소 이동 거리를 계산하고 출력
print(dijkstra(D, graph))