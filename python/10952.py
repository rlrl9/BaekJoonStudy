a,b = map(int, input().split())
while 1:
    if (a==0)or(b==0):
        break
    else:
        print(a+b)
        a,b = map(int, input().split())