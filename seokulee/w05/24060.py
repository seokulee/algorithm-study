import sys
import math

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
answer = list()

def merge_sort(A : list):
    if (len(A) == 1):
        return A
    mid = math.ceil(len(A) / 2)

    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    return merge(left, right)

def merge(A, B):
    merged = []
    i = j = 0

    while (i < len(A) and j < len(B)):
        if (A[i] <= B[j]):
            merged.append(A[i])
            answer.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            answer.append(B[j])
            j += 1

    merged.extend(A[i:])
    merged.extend(B[j:])
    answer.extend(A[i:])
    answer.extend(B[j:])

    return merged

sorted_arr = merge_sort(A)
print(answer[K-1] if K <= len(answer) else -1)
