a = int(input())
l1 = list(map(int,input().split()))
b = int(input())
l2 = list(map(int,input().split()))
d={}
for x in l1:
    d[x]='in'
for x in l2:
    if x in d:
        print(1,end=' ')
    else:
        print(0,end=' ')