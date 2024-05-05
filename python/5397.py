from collections import deque
for _ in range(int(input())):
    dq1=deque()
    dq2=deque()
    for c in input():
        if c == '<':
            if len(dq1):
                dq2.appendleft(dq1.pop())
        elif c == '>':
            if len(dq2):
                dq1.append(dq2.popleft())
        elif c == '-':
            if len(dq1):
                dq1.pop()
        else:
            dq1.append(c)
    print(''.join(dq1)+''.join(dq2))