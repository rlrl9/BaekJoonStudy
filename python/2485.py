import sys
input = sys.stdin.readline
import math
n = int(input())
f = int(input())
l=[]
sum=0
for i in range(n-1):
    a = int(input())
    l.append(a-f)
    f = a
b= l[0]
for i in range(1,len(l)):
    b = math.gcd(b,l[i])
for i in l:
    sum+=i//b-1
print(sum)