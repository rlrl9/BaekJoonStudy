n = int(input())
l = [25,10,5,1]
for _ in range(n):
    m = int(input())
    for j in range(len(l)):
        print(m//l[j],end=' ')
        m%=l[j]
    print()
    