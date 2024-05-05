n = int(input())
l=list(map(int,input().split()))
sort_l=sorted(list(set(l)))
d={sort_l[i]:i for i in range(len(sort_l))}
for x in l:
    print(d[x])