n = int(input())
min_x=10000
min_y=10000
max_x=-10000
max_y=-10000
for i in range(n):
    a,b=map(int,input().split())
    if min_x>a:
        min_x=a
    if max_x<a:
        max_x=a
    if min_y>b:
        min_y=b
    if max_y<b:
        max_y=b
print((max_x-min_x)*(max_y-min_y))