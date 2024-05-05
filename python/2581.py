min_n = int(input())
max_n = int(input())
f=[]
for i in range(min_n,max_n+1):
    for j in range(2,i+1):
        if i%j==0:
            if j==i:
                f.append(i)
            else:
                break
if sum(f)==0:
    print('-1')
else:
    print(sum(f))
    print(f[0])