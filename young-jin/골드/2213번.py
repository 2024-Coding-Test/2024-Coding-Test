import sys
input = sys.stdin.readline

n = int(input())
w = [0] + list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0,0] for _ in range(n+1)]
path = [[[] for _ in range(2)] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    dp[node][1] += w[node]
    # path[node][1] : node를 루트 노드로한 서브트리의 독립집합에 node가 포함된 경우
    path[node][1].append(node)

    for x in tree[node]:
        if not visited[x]:
            result = dfs(x)
            # 현재 노드를 추가하지 않을 경우, 자식 노드를 추가하는 경우와 추가하지 않는 경우 중 최댓값을 더함
            dp[node][0] += max(dp[x][0], dp[x][1])
            # 현재 노드를 추가할 경우, 자식 노드는 인접 노드이기 때문에 추가할 수 없으므로 추가하지 않는 경우를 더함
            dp[node][1] += dp[x][0]
            
            # path[node][0]과 path[node][1]에 어떤 경로를 더해야 하는지 결정
            # result[0] = path[x][0] : x를 루트 노드로한 서브트리의 독립집합에 x가 포함되지 않은 경우
            # result[1] = path[x][1] : x를 루트 노드로한 서브트리의 독립집합에 x가 포함된 경우
            # path[node][1]은 node를 포함하기 때문에 자식 노드인 x를 포함하지 않는 result[0]를 더하면 됨
            path[node][1] += result[0]
            # node를 포함하지 않는 경우인 path[node][0]에는 자식 노드가 포함되는 경우와 포함되지 않는 경우 둘 다 고려해야 함
            # 최댓값을 구하는 문제이기 때문에 자식 노드가 포함되는 경우와 포함되지 않는 경우 중 더 큰 값이 있는 경로를 더하면 됨
            if dp[x][0] > dp[x][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]

    return path[node]

# 임의로 루트 노드를 1로 설정
# dfs(1)의 리턴 값은 path[1]
p = dfs(1)
# 최댓값과 그에 해당하는 루트를 출력
# 루트 노드를 포함하는 경우와 포함하지 않는 경우를 비교해서 더 큰 값이 있는 경우를 출력
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    p[0].sort()
    print(*p[0])
else:
    print(dp[1][1])
    p[1].sort()
    print(*p[1])