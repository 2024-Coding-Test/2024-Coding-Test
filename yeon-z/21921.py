# 블로그를 시작하고 지난 일수 N과 X
# 블로그 시작 1일차부터 N일차까지 하루 방문자 수 공백 구분

from sys import stdin

N, X = map(int, stdin.readline().strip().split())
visited = list(map(int, stdin.readline().strip().split()))
intervalSum = sum(visited[0: X])
maxVisited = intervalSum
maxVisitedCount = 1


for i in range(1, N - X + 1):
    intervalSum = (intervalSum - visited[i-1]) + visited[i + X - 1]
    if intervalSum > maxVisited:
        maxVisited = intervalSum
        maxVisitedCount = 1
    elif intervalSum == maxVisited:
        maxVisitedCount += 1

if maxVisited == 0:
    print('SAD')
else:
    print(maxVisited)
    print(maxVisitedCount)
