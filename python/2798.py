n,m = map(int,input().split())
l=list(map(int,input().split()))
max_n=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if max_n<(l[i]+l[j]+l[k])<=m:
                max_n=l[i]+l[j]+l[k]
print(max_n)