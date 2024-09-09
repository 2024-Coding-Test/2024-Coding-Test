def solution(n, costs):
    # 간선들을 비용 기준으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    # Union-Find 자료구조 초기화
    # 각 노드의 부모를 자기 자신으로 설정 (초기에는 각 노드가 독립적인 집합)
    parent = list(range(n))

    # 노드의 최상위 부모를 찾는 함수
    def find(x):
        if parent[x] != x:  # 현재 노드가 루트가 아니라면
            parent[x] = find(parent[x])  # 경로 압축 최적화
        return parent[x]  # 최종적으로 찾은 루트 반환

    # 두 노드를 연결하는 함수
    def union(x, y):
        root_x, root_y = find(x), find(y)  # 각 노드의 루트를 찾음
        if root_x != root_y:  # 두 노드의 루트가 다르다면 (다른 집합이라면)
            parent[root_y] = root_x  # y의 루트를 x의 루트 아래에 붙임
            
    total_cost = 0  # 최소 신장 트리의 총 비용
    edges_used = 0  # 사용된 간선의 수
    
    # 크루스칼 알고리즘 수행
    for x, y, cost in costs:  # 비용이 작은 간선부터 순회
        # 두 노드가 아직 연결되지 않았다면
        if find(x) != find(y):
            union(x, y)  # 두 노드를 연결
            total_cost += cost  # 비용 추가
            edges_used += 1  # 사용된 간선 수 증가
            
        # 모든 노드가 연결되었다면 종료 (n-1개의 간선 사용)
        if edges_used == n - 1:
            break
            
    return total_cost