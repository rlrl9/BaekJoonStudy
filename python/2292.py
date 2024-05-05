n = int(input())
m=1
while True:
    if n==1:
        break
    elif (3*(m-1)*(m-2)+1)<n<(3*(m)*(m-1)+2):
        break
    else:
        m+=1
print(m)