n, m = map(int, input().split())
d = {}
d2 = {}

# n개의 문자열 입력 받기
for _ in range(n):
    a = input()
    d[a] = 1

# m개의 문자열 입력 받기
for _ in range(m):
    b = input()
    if b in d:  # 딕셔너리 d에 키가 있는지 확인
        d2[b] = 1

# 중복된 문자열의 개수 출력
print(len(d2))

# 중복된 문자열 출력
for i in sorted(d2):
    print(i)
