arr = [[0 for  i in range(100)] for j in range(100)]
n = int(input())
sum=0
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1
for j in range(100):
    sum+=arr[j].count(1)
print(sum)