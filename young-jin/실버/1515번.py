import sys
input = sys.stdin.readline

num = list(input().strip())
ans = 1

while True:
    for a in str(ans):
        if len(num) > 0 and a == num[0]:
            num.pop(0)
    
    if len(num) > 0:
        ans += 1
    else:
        print(ans)
        break