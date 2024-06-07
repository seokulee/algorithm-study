import sys

# for i in l:
#     if i in s:
#         print(1)
#     else:
#         print(0)


def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def main():
    N = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    s.sort()

    for i in lst:
        if binary_search(s, i, 0, len(s) - 1):
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()