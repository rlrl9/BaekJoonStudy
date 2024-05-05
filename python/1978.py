n = int(input())
l = list(map(int,input().split()))
f=[]
# 소수인지 판별하는 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 각 숫자가 소수인지 판별하여 리스트에 추가
for x in l:
    if is_prime(x):
        f.append(x)
print(len(f))