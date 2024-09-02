def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        # 스택의 최상단 요소가 현재 가격보다 큰 경우, 가격이 떨어졌음을 의미
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    # 스택에 남아 있는 요소들은 끝까지 가격이 떨어지지 않은 것
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1
    
    return answer
