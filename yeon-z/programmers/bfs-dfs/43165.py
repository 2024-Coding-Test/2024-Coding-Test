# 타겟 넘버
# 현재 코드
def solve(numbers, idx, current, target):
    if len(numbers) == idx:
        if target == current:
            global answer
            answer += 1
    else:
        solve(numbers, idx + 1, current + numbers[idx], target)
        solve(numbers, idx + 1, current - numbers[idx], target)


answer = 0


def solution(numbers, target):
    solve(numbers, 0, 0, target)
    return answer

# 이전 코드
answer = 0

def solution(numbers, target):
    def dfs(idx, cur):
        if len(numbers) == idx:
            if cur == target:
                global answer
                answer += 1
            return 0

        dfs(idx + 1, cur + numbers[idx])
        dfs(idx + 1, cur - numbers[idx])

    dfs(0, 0)

    global answer
    return answer