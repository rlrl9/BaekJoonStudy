import heapq
h = []
num = int(input())
for _ in range(num):
    for x in map(int,input().split()):
        if len(h) < num:
            heapq.heappush(h, x)
        else:
            heapq.heappushpop(h, x)
print(heapq.heappop(h))