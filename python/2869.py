up, dwn, total = map(int, input().split())

import math
day = math.ceil((total - up) / (up - dwn)) + 1

print(day)