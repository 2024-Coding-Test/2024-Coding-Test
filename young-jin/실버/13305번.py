n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))

# 지금 도시의 기름 가격이 이전 도시들의 기름 가격보다 높다면, 이전 도시의 기름 가격을 사용
# 반대의 경우에는 지금 도시의 기름 가격을 사용
# 처음 도시에서는 다음 도시로 가기 위해 무조건 기름을 넣어야 함

ans = price[0] * road[0]
low_price = price[0]
for i in range(1, n-1):
    if price[i] < low_price:
        ans += price[i] * road[i]
        low_price = price[i]
    else:
        ans += low_price * road[i]

print(ans)