l=list(map(int,input().split()))
l.sort()
if l[2]>=l[0]+l[1]:
    print((l[0]+l[1])*2-1)
else:
    print(sum(l))