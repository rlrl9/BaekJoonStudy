n, m= map(int,input().split())
arr=[]
def btr(start):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(start,n+1):
            arr.append(i)
            btr(i)
            arr.pop()
btr(1)