import sys
input = sys.stdin.readline

n,k,p,x = map(int,input().split())
# n : 1층~n층
# k : k자리 수 
# p : 최대 p개를 반전
# x : 실제로 멈춰있는 층

# LED로 표현된 숫자를 1차원 리스트로 변환
number = { 
    0 : [1,1,0,1,1,1,1],
    1 : [0,1,0,0,1,0,0],
    2 : [1,1,1,0,0,1,1],
    3 : [1,1,1,0,1,1,0],
    4 : [0,1,1,1,1,0,0],
    5 : [1,0,1,1,1,1,0],
    6 : [1,0,1,1,1,1,1],
    7 : [1,1,0,0,1,0,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,1,1,1,1,0]
}

# 숫자 i에서 j로 바꾸기 위해서 몇 개의 LED를 반전시켜야 하는지 계산
diff = {i : [0]*10 for i in range(10)}

for i in range(9):
    for j in range(i+1,10):
        cnt = 0
        for z in range(7):
            if number[i][z] != number[j][z]:
                cnt += 1
        diff[i][j] = cnt
        diff[j][i] = cnt

# 1부터 n까지 x에서 반전시킬 경우 바꿔야하는 LED의 수 구하기
tmp = []

x = str(x)
if len(x) < k:
    x = "0"*(k-len(x)) + x # 자릿수 맞춰서 0 추가
present_floor = list(int(s) for s in x)

for i in range(1,n+1):
    number_str = str(i)
    if len(number_str) < k:
        number_str = "0"*(k-len(number_str)) + number_str # 자릿수 맞춰서 0 추가
    if number_str != x: # 자기 자신으로 반전하는 경우는 제외
        tmp.append(number_str)

led_cnt = []
for t in tmp:
    cnt = 0
    for i, target in enumerate(t):
        a = present_floor[i] # 반전하기 전 숫자
        b = diff[a][int(target)] # 숫자 a에서 target으로 반전하기 위해 바꿔야하는 LED의 수
        cnt += b
    led_cnt.append(cnt)

# 최대 p개 반전된 경우만 카운트
ans = 0
ans_num = []
for i,cnt in enumerate(led_cnt):
    if cnt <= p:
        ans += 1
        ans_num.append(tmp[i])
print(ans)