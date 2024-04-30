import sys
import statistics



readline = sys.stdin.readline

N = int(readline())
arr = [int(readline()) for _ in range(N)]

print(round(statistics.mean(arr)))
print(statistics.median(arr))

mode = statistics.multimode(arr)
if len(mode) > 1:
    mode = sorted(mode)[1]

else:
    mode = mode[0]

print(mode)
print(max(arr) - min(arr))
