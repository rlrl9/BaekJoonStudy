s= input()
sum=0
l=['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for x in s:
    for i in l:
        if x in i:
            sum+=l.index(i)
            break
print(sum)