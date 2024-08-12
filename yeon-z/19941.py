# 햄버거 분배

from sys import stdin

# K 먹을 수 있는 거리
N, K = map(int, stdin.readline().strip().split())

tables = list(map(str, stdin.readline().strip()))
count = 0

for i in range(len(tables)):
    if tables[i] == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if tables[j] == 'H':
                tables[j] = 'X'
                count += 1
                break

print(count)