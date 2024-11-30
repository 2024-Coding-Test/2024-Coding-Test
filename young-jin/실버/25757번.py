import sys
input = sys.stdin.readline

n, game = input().strip().split()
name = set(input() for _ in range(int(n)))
l = len(name)

if game == 'Y':
    print(l)
elif game == 'F':
    print(l//2)
else:
    print(l//3)