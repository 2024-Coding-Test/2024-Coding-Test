from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for departure, arrival in tickets:
        graph[departure].append(arrival)
    
    for departure in graph:
        graph[departure].sort()
    
    def dfs(airport, path):
        # 모든 티켓을 사용했다면
        if len(path) == len(tickets) + 1:
            return path
        
        for i, next_airport in enumerate(graph[airport]):
            graph[airport].pop(i)

            new_path = dfs(next_airport, path + [next_airport])

            # new_path가 비어있지 않다면
            if new_path:
                return new_path
            
            graph[airport].insert(i, next_airport)
            
    return dfs("ICN", ["ICN"])