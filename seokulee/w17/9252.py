import sys

def solution(s1, s2):
    result = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])

    lcs_length = result[-1][-1]

    lcs = ''
    i, j = len(s2), len(s1)

    while i > 0 and j > 0:
        if s2[i - 1] == s1[j - 1]:
            lcs = s2[i - 1] + lcs
            i -= 1
            j -= 1
        elif result[i - 1][j] > result[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, lcs


if __name__ == '__main__':
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    lcs_length, lcs = solution(s1, s2)
    print(lcs_length)
    if lcs:
        print(lcs)
