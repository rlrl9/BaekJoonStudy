h, m = map(int,input().split())
t = int(input())
h=h+((m+t)//60)
if h>23:
    h=h-24
m=(m+t)%60
print(h,m)