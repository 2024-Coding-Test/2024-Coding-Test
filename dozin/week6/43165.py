from collections import deque
def solution(numbers, target):
    cnt = 0
    deq = deque([(0,0)])
    while deq:
        s,l = deq.popleft()
        if l>len(numbers):
            break
        if l==len(numbers) and target == s:
            cnt +=1
        deq.append((s+numbers[l-1],l+1))
        deq.append((s-numbers[l-1],l+1))
        
    return cnt