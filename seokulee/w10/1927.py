import sys
import heapq

N = int(sys.stdin.readline())
h = list()

for _ in range(N):
    num = int(sys.stdin.readline())

    if not num:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, num)
