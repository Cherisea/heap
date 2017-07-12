from heapq import *
from random import shuffle
date = list(range(10))
shuffle(date)
heap = []
for n in date:
    heappush(heap, n)
print(heap)