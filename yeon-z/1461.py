# 도서관 - 그리디
N, M = map(int, input().split())
books = list(map(int, input().split()))

answer = 0

plus = []
minus = []

for b in books:
    if b < 0:
        minus.append(b * -1)
    else:
        plus.append(b)

minus.sort(reverse=True)
plus.sort(reverse=True)

wait = []

temp = []
for i in range(len(minus)):
    if len(temp) < M:
        temp.append(minus[i])
    else:
        wait.append(max(temp))
        temp = [minus[i]]

if len(temp) > 0:
    wait.append(max(temp))

temp = []
for i in range(len(plus)):
    if len(temp) < M:
        temp.append(plus[i])
    else:
        wait.append(max(temp))
        temp = [plus[i]]
if len(temp) > 0:
    wait.append(max(temp))

wait.sort()

for w in wait[:-1]:
    answer += abs(w * 2)
answer += wait[-1]

print(answer)