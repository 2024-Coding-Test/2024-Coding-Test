def solution(tickets):
    
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        for i, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[i] == False:
                visited[i] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[i] = False
    
    dfs("ICN", ["ICN"])
    
    answer.sort()
    
    return answer[0]