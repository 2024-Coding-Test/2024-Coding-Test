# 쿠키의 신체 측정

# 출력
# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리

from sys import stdin
n = int(stdin.readline())
cookie = []
for i in range(n):
    cookie.append(list(stdin.readline().strip()))

head = [-1, -1]
for i in range(len(cookie)):
    for j in range(len(cookie[0])):
        if cookie[i][j] == '*':
            head[0] = i
            head[1] = j
            break
    if head[0] != -1:
        break

heart = [head[0]+1, head[1]]

# left Arm
leftArmStart = cookie[heart[0]].index('*')
leftArm = heart[1] - leftArmStart

# rightArm
rightArmStart = cookie[heart[0]][::-1].index("*")
rightArm = len(cookie[heart[0]]) - 1 - rightArmStart - heart[1]

# 허리
waist = 0
foot = -1
for i in range(heart[0]+1, len(cookie)):
    if cookie[i][heart[1]] == "*":
        waist += 1
    else:
        foot = i
        break

# 왼발
# i ~ len(cookie)
# heart[1] - 1
j = heart[1] - 1
leftFoot = 0
for i in range(foot, len(cookie)):
    if cookie[i][j] == "*":
        leftFoot += 1
    else:
        break

# 오른발
# i ~ len(cookie)
# heart[1] + 1
rightFoot = 0
j = heart[1] + 1
for i in range(foot, len(cookie)):
    if cookie[i][j] == "*":
        rightFoot += 1
    else:
        break
print(heart[0]+1, heart[1]+1)
print(leftArm, rightArm, waist, leftFoot, rightFoot)

