def is_prime(a):
    for j in range(2,int(math.sqrt(a))+1):
        if a%j==0:
            return False
    return True
import sys
import math
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a = int(input())
    while True:
        if a==0 or a==1:
            print(2)
            break
        else:
            if is_prime(a)==True:
                print(a)
                break
            else:
                a+=1