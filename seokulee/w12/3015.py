import sys
HEIGHT, CNT = 0, 1

def solution():
    stack = list()
    count = 0

    for i in range(N):
        while stack and stack[-1][HEIGHT] < A[i]:
            count += stack.pop()[CNT]

        if not stack:
            stack.append([A[i], 1])
            continue

        if stack[-1][HEIGHT] == A[i]:
            count += stack[-1][CNT]
            stack[-1][CNT] += 1

            if len(stack) > 1:
                count += 1
            # stack.append([A[i], 1])

        if stack[-1][HEIGHT] > A[i]:
            count += 1
            stack.append([A[i], 1])

    return count


N = int(sys.stdin.readline().rstrip())
A = list()
for _ in range(N):
    A.append(int(sys.stdin.readline().rstrip()))

print(solution())
