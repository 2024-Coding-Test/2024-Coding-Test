# 네트워크
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n
    wait = deque([0])

    while False in visited:
        if len(wait) == 0 and False in visited:
            answer += 1
            for idx in range(len(visited)):
                if visited[idx] == False:
                    wait.append(idx)
                    break

        cur = wait.popleft()
        visited[cur] = True

        for idx, c in enumerate(computers[cur]):
            if c == 1 and not visited[idx]:
                wait.append(idx)

    return answer + 1