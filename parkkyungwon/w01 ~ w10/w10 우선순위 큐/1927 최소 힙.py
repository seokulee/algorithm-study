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
            r = heapq.heappop(heap)

        sys.stdout.write(str(r) + '\n')
            
    else:
        heapq.heappush(heap, n)
