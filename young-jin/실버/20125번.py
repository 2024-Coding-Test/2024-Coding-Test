n = int(input())
cookie = [list(input()) for _ in range(n)]
heart = []
left_arm = []; right_arm = []
left_leg = []; right_leg = []
waist = []

for i in range(n):
    if len(heart) == 2:
        break
    for j in range(n):
        if cookie[i][j] == '*':
            heart.append(i+2)
            heart.append(j+1)
            break

print(*heart)

for i in range(n):
    if cookie[heart[0]-1][i] == '*':
        left_arm.append(heart[0])
        left_arm.append(i+1)
        break

for i in range(n-1,-1,-1):
    if cookie[heart[0]-1][i] == '*':
        right_arm.append(heart[0])
        right_arm.append(i+1)
        break

for i in range(n):
    if cookie[heart[0]-1+i][heart[1]-1] == '_':
        waist.append(heart[0]-1+i)
        waist.append(heart[1])
        break

for i in range(n):
    if waist[0]+i == n or cookie[waist[0]+i][waist[1]-2] == '_':
        left_leg.append(waist[0]+i)
        left_leg.append(waist[1]-1)
        break

for i in range(n):
    if waist[0]+i == n or cookie[waist[0]+i][waist[1]] == '_':
        right_leg.append(waist[0]+i)
        right_leg.append(waist[1]+1)
        break

print(heart[1]-left_arm[1], right_arm[1]-heart[1], waist[0]-heart[0], left_leg[0]-waist[0], right_leg[0]-waist[0])