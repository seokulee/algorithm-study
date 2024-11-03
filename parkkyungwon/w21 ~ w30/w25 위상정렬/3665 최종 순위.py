import sys



def sol(arr, data):
    leng = len(arr)

    dp = [0] * (leng+1)
    for i, v in enumerate(arr):
        dp[v] = i
    
    index = dp.copy()

    # 진입차수 dp의 값들은 항상 1, 2, 3, .. 순으로 1씩 증가한다.
    # 총 진입차수의 개수가 줄어든다면 ? 출력하는 경우가 발생한다.
    # 총 진입차수의 개수가 변하지 않는다면, 확실한 순위 순서이거나 불가능한 순서 밖에 존재하지 않는다.
    #
    # 1. 같은 쌍이 여러 번 발표되는 경우는 없다
    # 2. a와 b는 서로 다르다.
    # 1, 2 때문에 순위가 변동되어도, 총 진입차수의 개수는 변하지 않는다.
    # 따라서 ?를 출력하는 경우는 없다.
    for a, b in data:
        # 순위가 높은 팀이 b가 되도록 변경
        if index[a] < index[b]: a, b = b, a

        dp[a] -= 1
        dp[b] += 1
    
    if len(set(dp[1:])) == leng: 
        answer = [0] * leng

        for i, v in enumerate(dp[1:], 1):
            answer[v] = i

        return answer
        
    else: 
        return False


readline = sys.stdin.readline
write = sys.stdout.write
T = int(readline())

for _ in range(T):
    readline()
    arr = tuple(map(int, readline().split()))

    m = int(readline())
    data = tuple(map(int, readline().split()) for _ in range(m))

    answer = sol(arr, data)

    if answer: write(' '.join(map(str, answer)) + '\n')
    else: write('IMPOSSIBLE\n')
