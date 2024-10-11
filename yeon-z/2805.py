# 나무 자르기
N, M = map(int, input().split())

trees = list(map(int, input().split()))

s = 0
e = max(trees)

while s <= e:
    mid = (s + e) // 2
    # print(s, e, mid)
    result = 0
    for t in trees:
        if t > mid:
            result += (t - mid)
    if result == M:
        print(mid)
        exit()
    if result < M:
        e = mid - 1
    else:
        s = mid + 1
print(e)