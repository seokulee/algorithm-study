import sys



sys.setrecursionlimit(10**6)

N = int(input())
ino = tuple(map(int, input().split()))
posto = tuple(map(int, input().split()))

answer = []
ino_index = {v: i for i, v in enumerate(ino)}

def preo(in_s, in_e, post_s, post_e):
    if in_e == in_s: return

    # 후위의 맨마지막은 root
    root = posto[post_e-1]
    answer.append(root)
    
    # 중위에서 자식이 왼쪽과 오른쪽으로 나뉘는 인덱스를 찾기
    in_sep_idx = ino_index[root]
    post_sep_idx = in_sep_idx - in_s + post_s

    if in_sep_idx != in_s : preo(in_s, in_sep_idx, post_s, post_sep_idx)
    if in_sep_idx != in_e : preo(in_sep_idx+1, in_e, post_sep_idx, post_e-1)

preo(0, N, 0, N)

print(' '.join(map(str, answer)))
