# 삼성 기출
# 마법의 숲 탐색

# 6 5 6
# 2 3
# 2 0
# 4 2
# 2 0
# 2 0
# 2 2

# answer: 29

# --- default ----
from sys import stdin
input = stdin.readline
# ----------------

# --- prepare ---
R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
# ---- ----

# 상우하좌 (동쪽: 시계방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

exit_set = set()

def bfs(si, sj):
    q = []
    v = [[0] * (C + 2) for _ in range(R + 4)] # visited
    mx_i = 0 # -2 해서 리턴!

    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        mx_i = max(mx_i, ci)
        # 네방향, 미방문, 조건: 같은 값 또는 내가 출구 - 상대방이 골렘
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di , cj + dj
            if v[ni][nj] == 0 and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exit_set and arr[ni][nj] > 1)):
                v[ni][nj] = 1
                q.append((ni, nj))
    return mx_i - 2

ans = 0
num = 2
# 골렘 입력 좌표/방향에 따라서 남쪽 이동 및 정령 최대 좌표 계산/누적
for cj, dr in unit:
    ci = 1
    while True: # [1] 남쪽으로 최대한 이동(남쪽 -> 서쪽 -> 동쪽)
        # 남쪽(아래쪽)으로 한칸 이동
        if arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1] == 0: # 이동할 위치가 비어있다.
            ci += 1
        # 서쪽(왼쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj-1] + arr[ci][cj-2] + arr[ci+1][cj-2] + arr[ci+1][cj-1] + arr[ci+2][cj-1]) == 0:
            ci += 1
            cj -= 1
            dr = (dr-1) % 4
        # 동쪽(오른쪽)으로 회전하면서 아래로 한칸
        elif (arr[ci-1][cj+1] + arr[ci][cj+2] + arr[ci+1][cj+1] + arr[ci+1][cj+2] + arr[ci+2][cj+1]) == 0:
            ci += 1
            cj += 1
            dr = (dr + 1) % 4
        else:
            break
    # [2] 골렘을 표시 + 비상구위치 추가
    if ci < 4: # 몸이 범위밖으로 빠져나간 것 (새롭게 탐색시작.. arr 초기화)
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        num = 2
        exit_set = set()
    else:
        arr[ci+1][cj]=arr[ci-1][cj] = num
        arr[ci][cj-1:cj+2] = [num] * 3
        num += 1
        exit_set.add((ci+di[dr], cj+dj[dr]))
        ans += bfs(ci, cj)

print(ans)