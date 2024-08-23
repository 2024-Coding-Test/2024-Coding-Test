# 주식
# 1. 주식 하나를 산다.
# 2. 원하는 만큼 가지고 있는 주식을 판다.
# 3. 아무것도 안한다.

# 최대 이익 계산
# 예를 들어 날 수가 3일이고, 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다.
# 그러남 만약 날 별로 주가가 3, 5, 9 일때는 처음 두 날에 주식 하나씩 사고, 마지막날 다 팔아버리면 이익이 10이 된다.

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    money = 0
    stocks = list(map(int, stdin.readline().strip().split()))

    while stocks:
        if len(set(stocks)) == 1:
            break
        maxStock = max(stocks)
        maxStockIdx = stocks.index(maxStock)
        budgets = stocks[:maxStockIdx]
        for b in budgets:
            money += maxStock - b
        stocks = stocks[maxStockIdx+1:]
    print(money)