import sys
import heapq
from collections import defaultdict


readline = sys.stdin.readline

for _ in range(int(readline())):
    gheap = []
    lheap = []
    exist = defaultdict(int)
    count = 0

    for _ in range(int(readline())):
        command = readline().split()
        command[1] = int(command[1])

        if command[0] == 'I':
            heapq.heappush(gheap, -command[1])
            heapq.heappush(lheap, command[1])
            exist[command[1]] += 1
            count += 1

        elif count:
            if command[1] < 0: 
                while exist[v := heapq.heappop(lheap)] < 1: pass

            else: 
                while exist[v := -heapq.heappop(gheap)] < 1: pass

            exist[v] -= 1
            count -= 1
            
            if not count:
                gheap = []
                lheap = []
                exist = defaultdict(int)

    if count:
        while exist[smallest := heapq.heappop(lheap)] < 1: pass
        while exist[greatest := -heapq.heappop(gheap)] < 1: pass
        answer = f'{greatest} {smallest}\n' 

    else:
        answer = 'EMPTY\n'

    sys.stdout.write(answer)
