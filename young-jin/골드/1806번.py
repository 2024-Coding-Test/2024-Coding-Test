import sys
input = sys.stdin.readline

N,S = map(int,input().split())
seq = list(map(int,input().split()))

start = 0; end = 0
answer = 1e9
cumul = 0

while True:
    if cumul >= S:
        answer = min(end-start,answer)
        cumul -= seq[start]
        start += 1
        if answer == 1:
            break
    else:
        if end == N:
            break
        else:
            cumul += seq[end]
            end += 1
            
if answer == 1e9:
    print(0)
else:
    print(answer)