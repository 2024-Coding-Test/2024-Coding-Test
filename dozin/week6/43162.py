from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    dq=deque()
    def BFS(start):
        dq.append(start)
        while dq:
            s=dq.popleft()
            if visited[s]==0:
                visited[s]=1
            for i in range(len(computers)):
                if computers[s][i]==1 and visited[i]==0:
                    dq.append(i)
    while 0 in visited:
        answer+=1
        BFS(visited.index(0))
    return answer