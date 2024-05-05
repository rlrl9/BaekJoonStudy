import sys
n= int(input())
l=[]
for i in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
for x in l:
    print(x)