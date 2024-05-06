import sys

N, M = map(int, sys.stdin.readline().split())

idx2pocketmon = dict()
pocketmon2idx = dict()

for i in range(N):
    pocketmon = sys.stdin.readline().rstrip()
    idx2pocketmon[i+1] = pocketmon
    pocketmon2idx[pocketmon] = i+1

for _ in range(M):
    input = sys.stdin.readline().rstrip()
    if input in pocketmon2idx.keys():
        print(pocketmon2idx[input])
    else: # 무조건 예외는 없다는 가정
        print(idx2pocketmon[int(input)])

# 예전 버전 : input 확인할 때 key값에서 확인하는지, 0~9 확인하는지가 다름
# 예전버전이 더 효율적일듯
# import sys

# N, M = map(int, (sys.stdin.readline().split()))

# idx_name = dict()
# name_idx = dict()

# for i in range(1, N+1):
#     name = sys.stdin.readline().rstrip()
#     idx_name[i] = name
#     name_idx[name] = i

# for j in range(M):
#     input = sys.stdin.readline().rstrip()
#     if input[0] >= '1' and input[0] <= '9':
#         print(idx_name[int(input)])
#     else:
#         print(name_idx[input])
