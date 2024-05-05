a = int(input())
sum = 0
num = list(map(int,input().split()))
n = int(input())
for i in num:
    if i==n:
        sum+=1
print(sum)