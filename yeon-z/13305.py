# N개의 도시 일직선 도로
# 왼쪽에서 오른쪽으로 이동

from sys import stdin

N = int(stdin.readline())
distance = list(map(int, stdin.readline().strip().split()))
city = list(map(int, stdin.readline().strip().split()))
pay = 0

coin = city[0]
for i in range(N-1):
    if coin > city[i]:
        coin = city[i]
    pay += distance[i] * coin

print(pay)