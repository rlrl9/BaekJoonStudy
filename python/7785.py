n = int(input())
d={}
for i in range(n):
    name, el = map(str,input().split())
    if el=='enter':
        d[name]=True
    else:
        del d[name]
d=sorted(d.keys(),reverse=True)
for x in d:
    print(x,end='\n')