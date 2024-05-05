while True:
    n = int(input())
    if n==-1:
        break
    else:
        l=[]
        for i in range(1,n):
            if n%i==0:
                l.append(i)
            else:
                pass
        if n==sum(l):
            print(f'{n} = 1',end='')
            for x in l[1:]:
                print(f' + {x}',end='')
            print()
        else:
            print(f'{n} is NOT perfect.',end='\n')