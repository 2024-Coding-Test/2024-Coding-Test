from collections import deque, defaultdict

def solution(n, edge):
    # 그래프를 인접 리스트 형태로 구축
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS 초기화
    distances = [-1] * (n + 1)  # 거리 배열, -1로 초기화 (미방문 상태)
    distances[1] = 0  # 시작 노드의 거리는 0
    queue = deque([1])  # BFS를 위한 큐에 시작 노드 추가
    
    # BFS 수행
    while queue:
        node = queue.popleft()  # 현재 노드 가져오기
        current_distance = distances[node]  # 현재 노드까지의 거리
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 노드
                distances[neighbor] = current_distance + 1  # 거리 업데이트
                queue.append(neighbor)  # 큐에 추가
    
    # 가장 먼 거리와 그 거리의 노드 수 계산
    max_distance = max(distances)  # 가장 먼 거리
    farthest_nodes_count = distances.count(max_distance)  # 가장 먼 거리의 노드 수
    
    return farthest_nodes_count