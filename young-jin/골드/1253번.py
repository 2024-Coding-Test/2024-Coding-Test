import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int,input().split()))
number = sorted(number)

# target 값을 정하고 그 값을 기준으로 투 포인터 탐색
answer = 0
for i in range(N):
    target = number[i]
    start = 0; end = N-1
    while start < end:
        num_sum = number[start] + number[end]
        if num_sum == target:
            # target 수와 start 또는 end 수가 같으면 안 됨
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif num_sum > target:
            end -= 1
        elif num_sum < target:
            start += 1

print(answer)