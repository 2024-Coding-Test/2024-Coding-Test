# A와 B 2
# 문자열 S, T
# 1. 문자열 뒤에 A추가
# 2. 문자열 뒤에 B추가, 문자열 뒤집기


from sys import stdin

S = stdin.readline().strip()
T = stdin.readline().strip()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)