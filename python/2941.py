s = input()
word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for x in word:
    s=s.replace(x,'*')
print(len(s))