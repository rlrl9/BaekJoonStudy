n = int(input())
l = [0 for _ in range(101)]
l[1]=1
l[2]=1
l[3]=1
l[4]=2
for i in range(5,101):
    l[i]=l[i-1]+l[i-5]
for i in range(n):
    a= int(input())
    print(l[a])
