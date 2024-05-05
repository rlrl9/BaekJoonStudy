import sys
input=sys.stdin.readline
s = input().rstrip()
ss=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        ss.add(s[i:j+1])
print(len(ss))