while True:
    l = list(map(int,input().split()))
    if l[0]==0 and l[1]==0:
        break
    elif max(l)%min(l)==0:
        if l.index(max(l))==0:
            print('multiple')
        else:
            print('factor')
    else:
        print('neither')