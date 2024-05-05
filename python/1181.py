n=int(input())
l=[]
for _ in range(n):
    l.append(input())
l=list(set(l))
l.sort()
l.sort(key=len)
for x in l:
    print(x)