n, m = map(int, input().split())
l = list(map(int, input().split()))

# 입력받은 리스트를 정렬하고 뒤집음
l.sort(reverse=True)

# m번째로 큰 값 출력
print(l[m - 1])