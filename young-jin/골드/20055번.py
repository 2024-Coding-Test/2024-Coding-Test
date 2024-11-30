import sys
from collections import deque, Counter

input = sys.stdin.readline

n,k = map(int,input().split())
a = deque(map(int,input().split()))
robot = deque([0] * n)

ans = 0
while Counter(a)[0] < k:
    ans += 1
    a.rotate()
    robot.rotate()
    
    if robot[n-1] == 1:
        robot[n-1] = 0
        
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and a[i+1] != 0:
            robot[i] = 0
            robot[i+1] = 1
            a[i+1] -= 1

    if robot[n-1] == 1:
        robot[n-1] = 0

    if a[0] != 0:
        robot[0] = 1
        a[0] -= 1
        
print(ans)