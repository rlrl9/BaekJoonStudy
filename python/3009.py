x=[]
y=[]
for i in range(3):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
for j in x:
    if x.count(j)==1:
        print(j)
for j in y:
    if y.count(j)==1:
        print(j)