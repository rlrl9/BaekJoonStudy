n, m= map(int,input().split())
arr=[]
def btr():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(1,n+1):
            arr.append(i)
            btr()
            arr.pop()
btr()