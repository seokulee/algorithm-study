import sys

stack = list()
N = int(sys.stdin.readline())

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()

    if len(cmd) > 1:
        cmd, num = map(int, cmd.split())
    else:
        cmd = int(cmd)

    if cmd == 1:
        stack.append(num)
    elif cmd == 2:
        try:
            print(stack.pop())
        except:
            print(-1)
    elif cmd == 3:
        print(len(stack))
    elif cmd == 4:
        print(0 if len(stack) else 1)
    elif cmd == 5:
        try:
            print(stack[-1])
        except:
            print(-1)
