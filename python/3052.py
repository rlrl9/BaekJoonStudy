list=[0]*42
sum=0
for _ in range(10):
    list[int(input())%42] = 1
print(list.count(1))