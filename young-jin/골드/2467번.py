import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int,input().split()))

left_idx = 0
right_idx = n-1

ans = abs(liquid[left_idx] + liquid[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:
    tmp = liquid[left_idx] + liquid[right_idx]

    if abs(tmp) < ans:
        ans_left = left_idx
        ans_right = right_idx
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        left_idx += 1

    else:
        right_idx -= 1

print(liquid[ans_left], liquid[ans_right])