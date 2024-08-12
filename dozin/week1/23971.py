h,w,n,m = list(map(int,input().split(' ')))
import math
a = math.ceil(h/(n+1)) 
b = math.ceil(w/(m+1)) 
answer = a*b 
print(answer)