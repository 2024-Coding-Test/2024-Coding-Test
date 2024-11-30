import sys
sys.setrecursionlimit(10**6)

def get_sequence_value(n, p, q):
    cache = {}
    
    def dp(n):
        if n == 0:
            return 1
        if n in cache:
            return cache[n]
            
        # n//p와 n//q 계산
        p_val = n // p
        q_val = n // q
        
        # 새로운 값 계산 및 캐싱
        result = dp(p_val) + dp(q_val)
        cache[n] = result
        return result
    
    return dp(n)

# 입력 처리
n, p, q = map(int, input().split())
print(get_sequence_value(n, p, q))