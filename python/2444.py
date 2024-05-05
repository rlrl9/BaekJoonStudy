s= int(input())
for i in range(1,s+1):
    print(' '*(s-i)+'*'*(2*i-1))
for i in range(s+1,2*s):
    print(' '*(i-s)+'*'*((s*2-i)*2-1))