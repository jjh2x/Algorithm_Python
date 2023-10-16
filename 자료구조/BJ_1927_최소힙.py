import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
min_heap = []

for _ in range(n):
    x = int(input().strip())

    if x == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))

        else:
            print(0)

    else:
        heapq.heappush(min_heap, x)