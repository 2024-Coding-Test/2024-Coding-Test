def solution(n, lost, reserve):
    
    Arr = [1] * (n + 2)
    
    for r in reserve:
        Arr[r] += 1
    
    for l in lost:
        Arr[l] -= 1
    
    for i in range(1, n + 1):
        if Arr[i - 1] == 0 and Arr[i] == 2:
            Arr[i - 1], Arr[i] = 1, 1
        elif Arr[i] == 2 and Arr[i + 1] == 0:
            Arr[i], Arr[i + 1] = 1, 1
    
    answer = n - Arr.count(0)
    return answer