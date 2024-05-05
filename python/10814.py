n = int(input())
l=[]
for _ in range(n):
    year, name= map(str,input().split())
    l.append((int(year),name))
l.sort(key = lambda x:x[0])
for x in l:
    print(x[0], x[1])