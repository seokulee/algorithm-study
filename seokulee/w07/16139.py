import sys

# 50점 짜리 코드
# S = sys.stdin.readline().rstrip()
# q = int(sys.stdin.readline())
#
# for _ in range(q):
#     a, l, r = sys.stdin.readline().rstrip().split()
#
#     print(S[int(l):int(r)+1].count(a))


# 100점 코드
def solution():
    S = sys.stdin.readline().rstrip()
    q = int(sys.stdin.readline())
    alpha = [[0] * 26]

    for idx, char in enumerate(S):
        alpha.append(alpha[idx][:])
        alpha[idx+1][ord(char)-97] += 1

    for i in range(q):
        char, l, r = sys.stdin.readline().rstrip().split()
        l, r = int(l), int(r)
        print(alpha[r+1][ord(char)-97] - alpha[l][ord(char)-97])


if __name__ == '__main__':
    solution()