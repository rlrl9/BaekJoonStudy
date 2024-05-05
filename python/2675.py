num = int(input())
for _ in range(num):
    a,b = input().split()
    for i in b:
        print(i*int(a),end='')
    print()