def solution(n, costs):
    answer = 0
    bridge = 0
    cycle = {k:k for k in range(n)} 
    costs.sort(key=lambda x : x[2]) 
    for i in costs:
        if i[0] > i[1]: 
            i[0], i[1] = i[1], i[0]
        if cycle[i[1]] == cycle[i[0]]:
            continue
        answer += i[2]
        bridge += 1 
        past = cycle[i[1]] 
        cycle[i[1]] = cycle[i[0]] 
        for k, v in cycle.items(): 
            if v==past:
                cycle[k]=cycle[i[0]]
        if bridge == n-1:
            break
    return answer