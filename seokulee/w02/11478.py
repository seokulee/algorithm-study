import sys

S = sys.stdin.readline().rstrip()

L = len(S)
subset = set()

for i in range(L):
    for j in range(1, L+1):
        if i + j > L:
            break;
        subset.add(S[i:i+j])

print(len(subset))
