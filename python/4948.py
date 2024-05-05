import sys
import math
input=sys.stdin.readline
def is_prime(a):
    for j in range(2,int(math.sqrt(a))+1):
        if a%j==0:
            return False
    return True
l=list(range(2,246913))
total=[]
for i in l:
    if is_prime(i):
        total.append(i)
while True:
    n=int(input())
    if n==0:
        break
    sum=0
    for i in total:
        if n<i<2*n+1:
            sum+=1
    print(sum)