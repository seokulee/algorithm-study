no_heard_count, no_seen_count = map(int, input().split())

no_heard = {input() for _ in range(no_heard_count)}
no_seen = {input() for _ in range(no_seen_count)}

result = sorted(no_heard.intersection(no_seen))
print(len(result))
for r in result:
    print(r)
