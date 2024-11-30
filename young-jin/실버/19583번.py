import sys
input = sys.stdin.readline

S,E,Q = input().strip().split()

s_hour, s_min = S.split(':')
e_hour, e_min = E.split(':')
q_hour, q_min = Q.split(':')

s = int(s_hour) * 60 + int(s_min)
e = int(e_hour) * 60 + int(e_min)
q = int(q_hour) * 60 + int(q_min)

attend = dict()
while True:
    try:
        time, name = input().strip().split()
        t_hour, t_min = time.split(':')
        t = int(t_hour) * 60 + int(t_min)
        
        if name not in attend:
            attend[name] = 0

        if 0 <= t <= s:
            if attend[name] == 0:
                attend[name] += 1

        if e <= t <= q:
            if attend[name] == 1:
                attend[name] += 1
    except:
        break

ans = 0
for k,v in attend.items():
    if v >= 2:
        ans += 1

print(ans)