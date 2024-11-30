import sys
input = sys.stdin.readline

# N : 가로, M : 세로, L : 한 변의 길이, K : 별똥별 개수
N,M,L,K = map(int,input().split())
star = [list(map(int,input().split())) for _ in range(K)]

ans = K
for x,_ in star:
    for _,y in star:
        tmp = K
        for a,b in star:
            if x <= a <= x+L and y <= b <= y+L:
                tmp -= 1
        ans = min(ans,tmp)

print(ans)