n, m = map(int,input().split())
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = []
while n>0:
    l.append(n%m)
    n//=m
for i in l[::-1]:
    print(num_list[i],end='')