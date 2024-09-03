import sys
import heapq


readline = sys.stdin.readline
heap = []

for _ in range(int(readline())):
    n = int(readline())

    if n == 0:
        if len(heap) == 0:
            r = 0
        else:
            n, sign = heapq.heappop(heap)
            r = n * (1 if sign else -1)

        sys.stdout.write(str(r) + '\n')
        continue
            
    n = (abs(n), n > 0)
    heapq.heappush(heap, n)
