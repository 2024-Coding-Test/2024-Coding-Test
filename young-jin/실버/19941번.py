import sys
input = sys.stdin.readline

n,k = map(int,input().split())
table = list(input().strip())

ans = 0
for i in range(n):
    if table[i] == 'P':
        if i < k:
            end = i+k+1
            if end > n:
                end = n
            for j in range(end):
                if table[j] == 'H':
                    table[j] = 'X'
                    ans += 1
                    break
        elif i >= n-k:
            for j in range(i-k, n):
                if table[j] == 'H':
                    table[j] = 'X'
                    ans += 1
                    break
        else:
            for j in range(i-k, i+k+1):
                if table[j] == 'H':
                    table[j] = 'X'
                    ans += 1
                    break
print(ans)