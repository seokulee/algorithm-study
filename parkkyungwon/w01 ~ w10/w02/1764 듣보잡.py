import sys


readline = sys.stdin.readline
no_heard_count, no_seen_count = map(int, readline().split())

no_heard = {readline() for _ in range(no_heard_count)}
no_seen = {readline() for _ in range(no_seen_count)}

result = sorted(no_heard.intersection(no_seen))

print(len(result))
print(*result, sep='')
