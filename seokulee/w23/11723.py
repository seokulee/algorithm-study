import sys

M = int(sys.stdin.readline())
S = 0

for _ in range(M):
    line = sys.stdin.readline().strip()

    if ' ' in line:
        cmd, n = line.split()
        n = int(n)
    else:
        cmd = line

    if cmd == 'add':
        S |= (1 << (n - 1))
    elif cmd == 'remove':
        S &= ~(1 << (n - 1))
    elif cmd == 'check':
        print(1 if S & (1 << (n - 1)) else 0)
    elif cmd == 'toggle':
        S ^= (1 << (n - 1))
    elif cmd == 'all':
        S = (1 << 20) - 1
    elif cmd == 'empty':
        S = 0


# S = set()

# def add(n):
#     S.add(n)

# def remove(n):
#     S.discard(n)

# def check(n):
#     print(1 if n in S else 0)

# def toggle(n):
#     if n in S:
#         S.remove(n)
#     else:
#         S.add(n)

# def all_set():
#     global S
#     S = set(range(1, 21))

# def empty():
#     global S
#     S = set()

# for _ in range(M):
#     line = sys.stdin.readline().strip()

#     if ' ' in line:
#         cmd, n = line.split()
#         n = int(n)
#     else:
#         cmd = line

#     if cmd == 'add':
#         add(n)
#     elif cmd == 'remove':
#         remove(n)
#     elif cmd == 'check':
#         check(n)
#     elif cmd == 'toggle':
#         toggle(n)
#     elif cmd == 'all':
#         all_set()
#     elif cmd == 'empty':
#         empty()
