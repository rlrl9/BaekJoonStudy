a,b= input().split()
a_rev = ''.join(reversed(a))
b_rev = ''.join(reversed(b))
print(max(int(a_rev),int(b_rev)))