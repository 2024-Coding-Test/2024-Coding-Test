import sys

M = int(input())
S = [0 for _ in range(21)]

def add(x):
    if S[x] == 0:
        S[x] = 1

def remove(x):
    if S[x] == 1:
        S[x] = 0

def check(x):
    print(1 if S[x] == 1 else 0)

def toggle(x):
    S[x] = 1 - S[x]

def all():
    for i in range(1, 21):
        S[i] = 1

def empty():
    for i in range(1, 21):
        S[i] = 0

for _ in range(M):
    operation = sys.stdin.readline().strip().split()
    
    if operation[0] == "add":
        add(int(operation[1]))
    elif operation[0] == "remove":
        remove(int(operation[1]))
    elif operation[0] == "check":
        check(int(operation[1]))
    elif operation[0] == "toggle":
        toggle(int(operation[1]))
    elif operation[0] == "all":
        all()
    elif operation[0] == "empty":
        empty()