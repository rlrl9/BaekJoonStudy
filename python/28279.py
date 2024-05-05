import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])
for i in range(n):
    s = input().split()
    if s[0]=='1':
        queue.appendleft(s[1])
    elif s[0]=='2':
        queue.append(s[1])
    elif s[0]=='3':
        print(queue.popleft() if queue else -1)
    elif s[0]=='4':
        print(queue.pop() if queue else -1)
    elif s[0]=='5':
        print(len(queue))
    elif s[0]=='6':
        print(0 if queue else 1)
    elif s[0]=='7':
        print(queue[0] if queue else -1)
    elif s[0]=='8':
        print(queue[-1] if queue else -1)