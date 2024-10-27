def sol(data):
    count = 0
    visited = [False] * 8
    visited[0] = True
    compare = [0] * 8
    compare[0] = data[0]

    def dfs(depth):
        nonlocal count

        if depth == 8:
            for i in range(2):
                n1, n2, n3 = compare[i-2], compare[i-1], compare[i]
                
                if 2*(n1*n3)**2 - (n2*(n1 + n3))**2 > 0: break
            
            else:
                count += 1

            return
        
        for i in range(1, 8):
            if visited[i]: continue

            compare[depth] = data[i]
            if depth > 1:
                n1, n2, n3 = compare[depth-2], compare[depth-1], compare[depth]

                if 2*(n1*n3)**2 - (n2*(n1 + n3))**2 > 0: continue
            
            visited[i] = True
            dfs(depth + 1)
            visited[i] = False

    dfs(1)
    
    # s를 기준으로 회전된 경우를 고려해서 8을 곱해준다
    return 8*count

data = tuple(map(int, input().split()))

print(sol(data))
