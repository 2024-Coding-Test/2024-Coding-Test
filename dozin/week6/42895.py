import sys
from itertools import product
input = sys.stdin.readline

def solution(N, number):
    answer = 1
    DP = [set() for _ in range(9)]
    DP[1].add(N)
    
    if N == number:
        return answer
    
    
    for cal_cnt in range(2, 9):
        answer += 1
       
        DP[cal_cnt].add(int(str(N)*cal_cnt))
        
        
        for i in range(1, cal_cnt):
            j = cal_cnt - i
            
            
            for x, y in product(DP[i], DP[j]):
                DP[cal_cnt].update({x+y, x-y, x*y})
                
                if y != 0:
                    DP[cal_cnt].add(x//y)
            
            if number in DP[cal_cnt]:
                return answer
        
    return -1