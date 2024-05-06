import sys
import statistics

N = int(sys.stdin.readline())
arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 반올림한 값
print(round(statistics.mean(arr)))
print(statistics.median(arr))
modes = statistics.multimode(arr)
modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])
print(max(arr) - min(arr))
