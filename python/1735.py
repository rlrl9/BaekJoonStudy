def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x;
a,b = map(int,input().split())
c,d = map(int,input().split())
n = gcd(a*d+c*b,b*d)
print((a*d+c*b)//n,b*d//n)