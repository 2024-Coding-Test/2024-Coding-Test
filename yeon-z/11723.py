from sys import stdin

n = int(stdin.readline())
S = set()

for _ in range(n):
    commands = stdin.readline().strip().split(' ')
    match commands[0]:
        case 'all':
            S = set([i for i in range(1, 21)])
        case 'add':
            if int(commands[1]) not in S:
                S.add(int(commands[1]))
        case 'remove':
            if int(commands[1]) in S:
                S.remove(int(commands[1]))
        case 'check':
            if int(commands[1]) in S:
                print(1)
            else:
                print(0)
        case 'toggle':
            if int(commands[1]) in S:
                S.remove(int(commands[1]))
            else:
                S.add(int(commands[1]))
        case 'empty':
            S = set([])