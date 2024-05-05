n = int(input())
d = {}

# n번 반복하면서 딕셔너리에 키와 값의 쌍으로 추가
for _ in range(n):
    x, y = map(int, input().split())
    if x not in d:
        d[x] = []
    d[x].append(y)

# 딕셔너리의 키를 정렬
sorted_keys = sorted(d.keys())

# 정렬된 키에 대해 해당하는 값을 정렬하고 출력
for key in sorted_keys:
    values = sorted(d[key])
    for value in values:
        print(key, value)
