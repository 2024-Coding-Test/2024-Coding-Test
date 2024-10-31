# 카드게임
# 빨간, 파란, 노란, 녹색 네 가지 색의 카드 9장씩(1~9)
# 총 36개의 카드
# 36장의 카드에서 5장을 뽑고 아래와 같은 규칙으로 정수를 계산
# R, B, Y, G
from sys import stdin
cardsColor = []
cardsNumber = []
for _ in range(5):
    color, number = map(str, stdin.readline().split())
    cardsColor.append(color)
    cardsNumber.append(int(number))

temp = cardsNumber
temp.sort()
# 카드 5장이 모두 같은 색
if len(set(cardsColor)) == 1:
    # 1. 숫자가 연속적
    cnt = 0
    for i in range(len(temp)-1):
        if temp[i] + 1 == temp[i+1]:
            cnt += 1
        else:
            break
    if cnt == 4:
        print(900 + temp[-1])
        exit()

    # 4. 색이 모두 같은 경우, 가장 높은 숫자에 600을 더함
    print(600 + temp[-1])
    exit()

if len(set(cardsNumber)) == 2:
    # 2. 카드 5장 중 4장의 숫자가 같을 때
    setNumber = list(set(cardsNumber))
    a = setNumber[0]
    b = setNumber[1]
    if cardsNumber.count(a) == 4 or cardsNumber.count(b) == 4:
        if cardsNumber.count(a) == 4:
            print(800 + a)
            exit()
        else:
            print(800 + b)
            exit()
    # 3. 카드 3장의 숫자가 같고, 나머지 2장도 숫자가 같은 경우
    if cardsNumber.count(a) == 3:
        print((a * 10) + b + 700)
        exit()
    else:
        print((b * 10) + a + 700)
        exit()

# 5. 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다.
cnt = 0
for i in range(len(temp)-1):
    if temp[i] + 1 == temp[i+1]:
        cnt += 1
    else:
        break
if cnt == 4:
    print(500 + temp[-1])
    exit()

# 6. 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
setNumber = list(set(cardsNumber))
for s in setNumber:
    if cardsNumber.count(s) == 3:
        print(400 + s)
        exit()
# 7. 5장 중 2장의 숫자가 같고, 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 작은 숫자를 더한 다음 300을 더한다.
hubo = []
for s in setNumber:
    if cardsNumber.count(s) == 2:
        hubo.append(s)
if len(hubo) == 2:
    if hubo[0] > hubo[1]:
        print((hubo[0] * 10) + hubo[1] + 300)
        exit()
    else:
        print((hubo[1] * 10) + hubo[0] + 300)
        exit()

# 8. 카드 5장 중 2장의 숫자가 같을때 점수는 같은 숫자에 200을 더한다.
for s in setNumber:
    if cardsNumber.count(s) == 2:
        print(200 + s)
        exit()
print(100 + max(cardsNumber))