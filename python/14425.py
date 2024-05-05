n, m = map(int,input().split())
l=[]
sum=0
for i in range(n):
    l.append(input())
for i in range(m):
    if input() in l:
        sum+=1
print(sum)