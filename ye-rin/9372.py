import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())  # N: 국가의 수, M: 항공편의 수

    # 항공편 정보 입력
    for __ in range(M):
        u, v = map(int, input().split())

    # 항상 N - 1개의 항공편이 필요
    print(N - 1)