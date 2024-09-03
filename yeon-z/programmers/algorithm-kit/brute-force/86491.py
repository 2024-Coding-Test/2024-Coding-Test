# 최소직사각형
# 현재 코드
def solution(sizes):
    width = 0
    height = 0
    for s in sizes:
        s.sort()
        w, h = s
        width = max(width, w)
        height = max(height, h)

    return width * height

# 이전 코드
def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
    w = [s[0] for s in sizes]
    h = [s[1] for s in sizes]
    return  max(w) * max(h)