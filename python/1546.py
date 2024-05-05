num = int(input())
listN = list(map(int,input().split()))
average = sum(listN)/max(listN)
print((average/num)*100)