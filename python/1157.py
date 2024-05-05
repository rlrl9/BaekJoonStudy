s = input().upper()
l={}
sum=0
same=0
xs = ''
for x in s:
    if x in l:
        l[x]+=1
    else:
        l[x]=1
for x in l:
    if sum<l[x]:
        sum=l[x]
        xs=x
    elif sum==l[x]:
        same=sum
if sum==same:
    print('?')
else:
    print(xs)