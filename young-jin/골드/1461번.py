import sys
input = sys.stdin.readline

N,M = map(int,input().split())
book = list(map(int,input().split()))
answer = []
ans = 0

book = sorted(book)
minus = []
plus = []

for b in book:
    if b < 0:
        minus.append(b)
    else:
        plus.append(b)

len_m = len(minus)
len_p = len(plus)

if len_m % M != 0:
    answer.append(min(minus[-(len_m % M):]))

if len_p % M != 0:
    answer.append(max(plus[:(len_p % M)]))

for i in range(len_m // M):
    answer.append(min(minus[M*i:M*(i+1)]))

plus = plus[(len_p % M):]
for i in range(len_p // M):
    answer.append(max(plus[M*i:M*(i+1)]))

answer = sorted(list(map(abs, answer)))

ans += answer.pop() + sum(answer)*2
print(ans)