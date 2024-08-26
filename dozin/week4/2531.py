import sys 
input = sys.stdin.read

data = input().splitlines()
n, d, k, c = map(int, data[0].split())
sushi = [int(x) for x in data[1:]]

max_cnt = 0
for i in range(n):
    if i <= n - k:
        sets = set(sushi[i:i + k])
    else:
        sets = set(sushi[i:])
        sets.update(sushi[:(i + k) % n])
    
    sets.add(c)
    max_cnt = max(max_cnt, len(sets))

print(max_cnt)