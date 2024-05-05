a, b = map(int, input().split())
l = [list(input()) for _ in range(a)]
count = []
for i in range(a - 7):
    for j in range(b - 7):
        n1 = 0
        n2 = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if l[x][y] != 'W':
                        n1 += 1
                    else:
                        n2 += 1
                else:
                    if l[x][y] != 'B':
                        n1 += 1
                    else:
                        n2 += 1
        count.append(min(n1, n2))
print(min(count))
