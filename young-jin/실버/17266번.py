n = int(input())
m = int(input())
x = list(map(int, input().split()))

if m == 1:
    print(max(x[0], n-x[0]))
else:
    ans = []
    ans.append(x[0])

    for i in range(m-1):
        interval = x[i+1] - x[i]
        if interval%2 == 0:
            ans.append(interval//2)
        else:
            ans.append(interval//2 + 1)

    ans.append(n-x[-1])

    print(max(ans))

# 신호등 사이의 간격을 생각하면 쉽게 풀 수 있는 문제
# 모든 거리를 비출 수 있는 간격을 구할려면 어떻게 해야 하는지 생각