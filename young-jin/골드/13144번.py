import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))

answer = 0
start = 0; end = 0
visited = [False] * (n+1)

while start <= end and end < n:
    if not visited[number[end]]:
        visited[number[end]] = True
        end += 1
        answer += end - start
    else:
        while visited[number[end]]:
            visited[number[start]] = False
            start += 1

print(answer)