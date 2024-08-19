import sys
input = sys.stdin.readline

num = int(input())
S = set()
for _ in range(num):
    task = list(input().strip().split())
    n = task[0]
    if len(task) > 1:
        m = int(task[1])

    if n == 'add':
        if m not in S:
            S.add(m)
        else:
            pass
    
    elif n == 'remove':
        if m in S:
            S.remove(m)
        else:
            pass
    
    elif n == 'check':
        if m in S:
            print(1)
        else:
            print(0)
    
    elif n == 'toggle':
        if m in S:
            S.remove(m)
        else:
            S.add(m)
    
    elif n == 'all':
        S = {i for i in range(1,21)}

    else:
        S.clear()