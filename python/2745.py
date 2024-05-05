a, b= input().split()
b= int(b)
sum=0
k=0
for x in a:
    try:
        sum+=int(x)*(b**(len(a)-1-k))
        k+=1
    except:
        sum+=(ord(x)-55)*(b**(len(a)-1-k))
        k+=1
print(sum)