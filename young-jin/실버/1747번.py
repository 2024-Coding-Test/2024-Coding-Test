import sys
input = sys.stdin.readline

N = int(input())

def isPalindrome(n):
    s = reversed(list(str(n)))
    reverse_n = int(''.join(s))
    if n == reverse_n:
        return True
    return False

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    if isPalindrome(N) and isPrime(N):
        print(N)
        break
    else:
        N += 1