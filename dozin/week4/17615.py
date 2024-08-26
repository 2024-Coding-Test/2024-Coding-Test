import sys 
input=sys.stdin.readline
n=int(input().strip())
balls=str(input().strip())
cnt=[]
r=balls.rstrip('R')
cnt.append(r.count('R'))
r=balls.rstrip('B')
cnt.append(r.count('B'))
l=balls.lstrip('R')
cnt.append(l.count('R'))
l=balls.lstrip('B')
cnt.append(l.count('B'))
print(min(cnt))

#rstrip(),lstrip(),strip()이용해서 푸는 방식 고민해보기 
