n = int(input())
request = list(map(int,input().split()))
budget = int(input())

# 처음부터 예산을 넘지 않을 때
if sum(request) <= budget:
    print(max(request))

# 넘을 경우
else:
    ans = []
    left = 0
    right = max(request)
    while left < right-1:
        mid = (left+right)//2
        total = 0
        for i in range(n):
            if request[i] >= mid:
                total += mid
            else:
                total += request[i]
        
        if total <= budget:
            ans.append(mid)
            left = mid
        else:
            right = mid

    print(max(ans))