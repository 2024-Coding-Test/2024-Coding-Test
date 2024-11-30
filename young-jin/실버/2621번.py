import sys
input = sys.stdin.readline

color = []; num = []
for _ in range(5):
    c,n = input().split()
    color.append(c)
    num.append(int(n))

# 숫자가 연속적인지 확인하는 함수
def is_consecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

ans = 0
# 카드 5장이 모두 같은 색이면서 숫자가 연속적인 경우
if len(set(color)) == 1 and is_consecutive(num):
    result = 900 + max(num)
    ans = max(ans, result)

# 카드 5장 중 4장의 숫자가 같은 경우
# 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때
if len(set(num)) == 2:
    for n in set(num):
        if num.count(n) == 4:
            result = 800 + n
            break
        elif num.count(n) == 3:
            result = 700 + (n*10) + (sum(set(num))-n)
            break

    ans = max(ans, result)

# 카드 5장의 색깔이 모두 같을 때
if len(set(color)) == 1:
    result = 600 + max(num)
    ans = max(ans, result)

# 카드 5장의 숫자가 연속적일 때
if is_consecutive(num):
    result = 500 + max(num)
    ans = max(ans, result)

# 카드 5장 중 3장의 숫자가 같을 때
# 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 경우
tmp = []
for n in set(num):
    if num.count(n) == 3:
        result = 400 + n
        ans = max(ans, result)
        break

    elif num.count(n) == 2:
        tmp.append(n)

if len(tmp) == 2:
    result = (max(tmp)*10) + min(tmp) + 300
    ans = max(ans,result)

# 카드 5장 중 2장의 숫자가 같을 때
for t in tmp:
    result = 200 + t
    ans = max(ans, result)

# 어떤 경우에도 해당하지 않을 때
result = 100 + max(num)
ans = max(ans, result)

print(ans)