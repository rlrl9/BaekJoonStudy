n,m = map(int,input().split())
arr = [[0 for i in range(m)] for j in range(n)]
arr2 = [[0 for i in range(m)] for j in range(n)]
arr3 = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        arr[i][j]=l[j]
for i in range(n):
    k = list(map(int,input().split()))
    for j in range(m):
        arr2[i][j]=k[j]
for i in range(n):
    for j in range(m):
        arr3[i][j]=arr[i][j]+arr2[i][j]
        print(arr3[i][j],end=' ')
    print()