import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # As
O = list(map(int, sys.stdin.readline().split())) #operators
results = list()
result = A[0]

def calculate(n, result):
    if n == N:
        results.append(result)
        return

    # result operator A[n]
    for i, numOp in enumerate(O):
        if numOp > 0:
            O[i] -= 1

            if i == 0:
                c_result = result + A[n]
            elif i == 1:
                c_result = result - A[n]
            elif i == 2:
                c_result = result * A[n]
            else:
                c_result = int(result / A[n])

            calculate(n+1, c_result)
            O[i] += 1

calculate(1, result)

print(max(results))
print(min(results))
