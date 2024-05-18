n = int(input())
num = list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
max_rs=-int(1e9)
min_rs=int(1e9)
def dfs(add,sub,mul,div,sum,i):
    global max_rs,min_rs
    if i==n:
        max_rs=max(max_rs,sum)
        min_rs=min(min_rs,sum)
        return
    else:
        if add:
            dfs(add-1,sub,mul,div,sum+num[i],i+1)
        if sub:
            dfs(add,sub-1,mul,div,sum-num[i],i+1)
        if mul:
            dfs(add,sub,mul-1,div,sum*num[i],i+1)
        if div:
            dfs(add,sub,mul,div-1,int(sum/num[i]),i+1)
dfs(add,sub,mul,div,num[0],1)
print(max_rs)
print(min_rs)