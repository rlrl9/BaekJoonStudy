n = int(input())
s = list(map(int,input().split()))
stack=[]
a =1
for i in s:
    stack.append(i)
    while stack and stack[-1]==a:
        stack.pop()
        a+=1
if stack:
    print('Sad')
else:
    print('Nice')