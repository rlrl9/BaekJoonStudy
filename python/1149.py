n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
l=[[0 for _ in range(3)] for _ in range(n)]
l[0]=arr[0]
for i in range(1,n):
    l[i][0]=min(l[i-1][1],l[i-1][2])+arr[i][0]
    l[i][1]=min(l[i-1][2],l[i-1][0])+arr[i][1]
    l[i][2]=min(l[i-1][0],l[i-1][1])+arr[i][2]
print(min(l[n-1]))