from collections import deque, defaultdict

def bfs(node, graph, n):
    # BFS를 사용하여 한쪽 부분의 노드 개수를 구하는 함수
    visited = [False] * (n + 1)  # 방문한 노드를 기록하는 리스트
    queue = deque([node])  # BFS를 위한 큐
    visited[node] = True  # 시작 노드 방문 표시
    count = 1  # 방문한 노드 수를 기록하는 변수
    
    while queue:
        current = queue.popleft()  # 큐에서 노드를 꺼냄
        
        # 현재 노드에 연결된 이웃 노드들을 확인
        for neighbor in graph[current]:
            if not visited[neighbor]:  # 이웃 노드가 방문되지 않은 경우
                visited[neighbor] = True  # 방문 표시
                queue.append(neighbor)  # 큐에 이웃 노드를 추가
                count += 1  # 방문한 노드 수 증가
    
    return count  # 해당 연결된 부분의 노드 수 반환

def solution(n, wires):
    min_difference = float('inf')  # 두 부분의 노드 개수 차이의 최소값을 저장할 변수
    
    # 주어진 모든 간선을 순차적으로 하나씩 제거하면서 최소 차이를 계산
    for i in range(len(wires)):
        # 그래프를 인접 리스트로 표현
        graph = defaultdict(list)
        
        # 특정 간선을 제거하고 나머지 간선으로 그래프를 구성
        for j in range(len(wires)):
            if i != j:  # i 번째 간선을 제거
                v1, v2 = wires[j]
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        # BFS를 통해 한쪽 부분의 노드 개수를 구함
        first_part_count = bfs(1, graph, n)
        
        # 전체 노드 수에서 첫 번째 부분의 노드 수를 빼서 다른 부분의 노드 수를 구함
        second_part_count = n - first_part_count
        
        # 두 부분의 차이의 절대값을 계산하고 최소값을 갱신
        min_difference = min(min_difference, abs(first_part_count - second_part_count))
    
    return min_difference  # 최소 차이를 반환