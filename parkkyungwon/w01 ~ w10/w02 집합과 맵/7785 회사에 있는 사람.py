count = int(input())

remains = {}
for _ in range(count):
    name, state = input().split()
    remains[name] = state

keys = sorted(remains.keys(), reverse=True)
for key in keys:
    if remains[key] == 'enter':
        print(key)
        