import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    if i+k > n:
        # set을 활용해서 c가 리스트에 중복 존재하는 경우를 지울 수 있음
        # 처음과 끝이 연결되어 있기 때문에 나머지를 활용해서 이어 줌
        ans = max(ans, len(set(sushi[i:] + sushi[:(i+k)%n] + [c]))) 
    else:
        ans = max(ans, len(set(sushi[i:i+k] + [c])))
print(ans)