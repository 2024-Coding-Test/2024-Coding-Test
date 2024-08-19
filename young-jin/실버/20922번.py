import sys
input = sys.stdin.readline

n,k = map(int,input().split())
sequence = list(map(int,input().split()))

left = 0; right = 0
ans = 0
count = {num : 0 for num in sequence}

while right < n:
    if count[sequence[right]] < k:
        count[sequence[right]] += 1
        right += 1
    else:
        count[sequence[left]] -= 1
        left += 1
    ans = max(ans, right-left)

print(ans)