n = int(input())
three = 0

while True:
    if n - three * 3 < 0:
        print(-1)
        break
    elif (n - three * 3) % 5 == 0:
        print(three + ((n - three * 3) // 5))
        break
    else:
        three += 1
