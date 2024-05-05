n = int(input())

for i in range(n):
    if n == i + sum(map(int, str(i))):
        print(i)
        break
    elif i == n-1:
        print(0)
