arr = []
for i in range(5):
    l=list(input())
    arr.append(l)
    arr[i] += [''] * (15 - len(l))
for i in range(15):
    for j in range(5):
        print(arr[j][i],end='')