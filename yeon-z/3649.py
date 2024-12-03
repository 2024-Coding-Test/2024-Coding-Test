# 로봇 프로젝트
from sys import stdin

while True:
    try:
        X = int(stdin.readline())
    except:
        break
    X *= 10000000

    N = int(stdin.readline())
    arr = [int(stdin.readline()) for _ in range(N)]
    arr.sort()

    result = []
    left, right = 0, N-1
    while left < right:
        if arr[left] + arr[right] < X:
            left += 1
        elif arr[left] + arr[right] > X:
            right -= 1
        else:
            result = [arr[left], arr[right]]
            break
    if result:
        print(f'yes {result[0]} {result[1]}')
    else:
        print('danger')
