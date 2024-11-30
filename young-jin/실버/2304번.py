n = int(input())
pillar = [list(map(int,input().split())) for _ in range(n)]

sorted_pillar = sorted(pillar, key=lambda x : x[0])

max_height = 0
for i in range(n):
    if max_height <= sorted_pillar[i][1]:
        max_height = sorted_pillar[i][1]
        idx = i

ans = 0
height = sorted_pillar[0][1]
for i in range(idx):
    if height <= sorted_pillar[i+1][1]:
        ans += (sorted_pillar[i+1][0] - sorted_pillar[i][0]) * height
        height = sorted_pillar[i+1][1]
    else:
        ans += (sorted_pillar[i+1][0] - sorted_pillar[i][0]) * height

height = sorted_pillar[n-1][1]
for j in range(n-1, idx, -1):
    if height <= sorted_pillar[j-1][1]:
        ans += (sorted_pillar[j][0] - sorted_pillar[j-1][0]) * height
        height = sorted_pillar[j-1][1]
    else:
        ans += (sorted_pillar[j][0] - sorted_pillar[j-1][0]) * height

print(ans + max_height)