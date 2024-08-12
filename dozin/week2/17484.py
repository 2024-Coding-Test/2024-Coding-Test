import sys

n, m = map(int, sys.stdin.readline().split())
arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
dir = [-1, 0, 1]

def dfs(col, row, d, answer):
    if col == n - 1:
        return answer
    low = int(sys.maxsize)
    for i in dir:
        if i != d:
            new_col, new_row = col + 1, row + i
            if 0 <= new_col < n and 0 <= new_row < m:
                low = min(low, dfs(new_col, new_row, i, answer + arr[new_col][new_row]))
    return low

low = int(sys.maxsize)
for i in range(m):
    low = min(dfs(0, i, 2, arr[0][i]), low)
print(low)
