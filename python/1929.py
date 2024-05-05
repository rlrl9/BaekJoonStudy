import sys
import math
input=sys.stdin.readline
def is_prime(a):
    for j in range(2,int(math.sqrt(a))+1):
        if a%j==0:
            return False
    return True
a,b=map(int,input().split())
for i in range(a,b+1):
    if i==1:
        pass
    elif is_prime(i):
        print(i,end='\n')