a,b = map(int,input().split())
res=a*b
while b!=0:
    a,b=b,a%b
print(res//a)