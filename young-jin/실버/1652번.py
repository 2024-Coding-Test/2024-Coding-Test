import sys
input = sys.stdin.readline

N = int(input())
room = [list(input().strip()) for _ in range(N)]

ans = [0,0]
for i in range(N):
    n_row = 0; n_col = 0
    for j in range(N):
        if room[i][j] == '.':
            n_row += 1
        else:
            n_row = 0
        if n_row == 2:
            ans[0] += 1

        if room[j][i] == '.':
            n_col += 1
        else:
            n_col = 0
        if n_col == 2:
            ans[1] += 1

print(*ans)

# 빈자리가 2개 이상인 경우 누울 수 있음
# 빈자리를 계속 더해가기 때문에 2개 이상인 경우를 세지 않고 2개인 경우를 세어야 함.
# 2개 이상인 경우와 2개인 경우 둘 다 누울 수 있는 자리 1개로 계산하기 때문