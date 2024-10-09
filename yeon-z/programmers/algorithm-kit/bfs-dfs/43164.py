# 여행 경로
from collections import defaultdict
def solution(tickets):
    # 티켓 정보를 딕셔너리로 변환
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append(end)

    # 각 출발지에 대해 도착지를 정렬
    for start in graph:
        graph[start].sort()

    path = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        path.append(airport)

    dfs('ICN')
    return path[::-1]

# 여행경로
from collections import defaultdict


def solution(tickets):
    # 티켓 정보를 딕셔너리로 변환
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append(end)

    # 각 출발지에 대해 도착지를 정렬
    for start in graph:
        graph[start].sort()

    def dfs(airport, path):
        # 모든 티켓을 사용한 경우
        if len(path) == len(tickets) + 1:
            return path
        # 현재 공항에서 갈 수 있는 다음 공항들을 탐색
        for i, next_airport in enumerate(graph[airport]):
            graph[airport].pop(i)
            new_path = dfs(next_airport, path + [next_airport])
            if new_path:
                return new_path
            # 백트래킹: 유효한 경로를 찾지 못했다면 티켓을 다시 추가
            graph[airport].insert(i, next_airport)

    return dfs('ICN', ['ICN'])
