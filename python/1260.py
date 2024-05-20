from collections import deque
n, m, v = map(int,input().split())
grh = [[False for _ in range(n+1)] for _ in range(n+1)]
visit1=[False for _ in range(n+1)]
visit2=[False for _ in range(n+1)]
for i in range(m):
    x, y= map(int,input().split())
    grh[x][y]=1
    grh[y][x]=1
def dfs(v):
    visit1[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if visit1[i]==False and grh[v][i]==1:
            dfs(i)
def bfs(v):
    q=deque([v])
    visit2[v]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visit2[i]==False and grh[v][i]==1:
                q.append(i)
                visit2[i]=True
dfs(v)
print()
bfs(v)