import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(len(s1-s2)+len(s2-s1))
