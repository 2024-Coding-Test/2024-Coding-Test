def solution(n, times):
    answer = 0
    times.sort(reverse=True)

    start = 1
    end = max(times) * n

    while start < end:
        mid = (start + end) // 2
        result = 0
        for a in times:
            result += mid // a

        if result >= n:
            end = mid
        else:
            start = mid + 1

    return start