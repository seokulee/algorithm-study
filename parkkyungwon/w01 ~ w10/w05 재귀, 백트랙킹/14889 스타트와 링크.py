import itertools



def find():
    h, v = [0]*N, [0]*N
    for i in range(N):
        for j in range(N):
            h[i] += mat[i][j]
            v[i] += mat[j][i]

    min_diff = 1e10
    oppoent_ori = sum(v)

    for case in itertools.combinations(range(N), N//2):
        opponent = oppoent_ori
        my = 0
        for i in case:
            my += h[i]
            opponent -= v[i]
        
        diff = abs(my - opponent)
        if diff < min_diff:
            min_diff = diff
    
    return min_diff


N = int(input())

mat = tuple(tuple(map(int, input().split())) for _ in range(N))

print(find())
