n,m=map(int,input().split())
list =[0]*n
for _ in range(m):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        list[j-1]=c
for i in range(n):
    print(list[i])