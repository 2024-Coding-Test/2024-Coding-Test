n = int(input())
switch = list(map(int,input().split()))

m = int(input())
for i in range(m):
    gender,number = map(int,input().split())
    
    if gender == 1:
        for i in range(1, (n//number)+1):
            if switch[(number*i)-1] == 0:
                switch[(number*i)-1] = 1
            else:
                switch[(number*i)-1] = 0
    
    else:
        s,e = number-1, number-1
        for i in range(1, number):
            if number-1+i >= n: # indexerror 방지
                break
            if switch[number-1-i] == switch[number-1+i]:
                s,e = number-1-i, number-1+i
            else: # 앞뒤 스위치 상태가 다르면 바로 중단
                break

        for i in range(s,e+1):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0

if n > 20:
    for i in range(n//20+1):
        print(*switch[20*i:20*(i+1)])
else:
    print(*switch)