s = input()
l = [-1]*26
for i in range(26):
    try: 
        l[i] = s.index(chr(97+i))
    except:
        l[i] = -1
for i in l:
    print(i)