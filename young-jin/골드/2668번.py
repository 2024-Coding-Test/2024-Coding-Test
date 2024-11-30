N = int(input())
table = {}

for i in range(1,N+1):
    num = int(input())
    table[i] = num

def dfs(table, visited, start, node, tmp, number):
    if table[node] == start:
        number.append(node)
        tmp.append(number)
        return 
    
    visited[node] = True
    number.append(node)
    if not visited[table[node]]:
        dfs(table, visited, start, table[node], tmp, number)

tmp = []
for i in table:
    number = []
    visited = [False] * (len(table)+1)
    # 같은 cycle이 포함되는 경우를 방지하기 위해 tmp에 추가된 cycle은 방문 표시 함.
    for j in range(len(tmp)):
        for z in tmp[j]:
            visited[z] = True
    dfs(table, visited, i, i, tmp, number)

ans = []
for i in tmp:
    ans += i

print(len(ans))
for i in sorted(ans):
    print(i)