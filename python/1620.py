import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d={}
for i in range(1,n+1):
    a = input().rstrip()
    d[a]=i
    d[str(i)]=a
for _ in range(m):
    p = input().rstrip()
    if p in d:
        print(d[p])