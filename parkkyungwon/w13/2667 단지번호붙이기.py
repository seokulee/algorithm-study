import sys



readline = sys.stdin.readline


def sol(arr, n):
    # 입력을 2진수로 간주하고 정수로 저장
    arr2 = tuple(int(a, 2) for a in arr)
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = [set() for _ in range(n**2)]

    # 좌표를 계산하기 위해 coordin 변수 사용
    # 가장 위, 오른쪽을 0으로 시작하고 왼쪽으로 1칸씩 좌표값이 1 증가.
    coordin = 0
    prev = 0
    for curr in arr2:
        # 2진수를 사용해서 연결된 정보를 저장
        # 위 아래가 1이면 연결됌
        v = prev & curr
        for i in range(n):
            if (v >> i) & 1:
                spot[coordin].add(coordin - n)
                spot[coordin - n].add(coordin)
            
            coordin += 1
        
        prev = curr
    
    coordin = 0
    for curr in arr2:
        # 좌 우가 1이면 연결됌
        h = curr & (curr >> 1)
        for i in range(n):
            if (h >> i) & 1:
                spot[coordin].add(coordin + 1)
                spot[coordin + 1].add(coordin)
            
            coordin += 1


    def bfs(a):
        hist_lst = [a]
        hist_set = {a, }
        
        # hist_lst에 순차적으로 다음 탐색할 정점을 추가
        for i in hist_lst:
            for j in spot[i]:
                if j in hist_set:
                    continue

                hist_lst.append(j)
                hist_set.add(j)
            
            # 방문했던 정점의 연결 정보 제거
            spot[i] = set()
        
        return len(hist_lst)


    answer = []
    for i in range(len(spot)):
        if spot[i]:
            answer.append(bfs(i))
    
    # 연결 점이 없는 점을 계산
    answer.extend([1] * (sum(a.count('1') for a in arr) - sum(answer)))

    # 정답을 오름차순으로 정렬
    answer.sort()
    
    return answer


n = int(readline())
a = tuple(readline() for _ in range(n))

answer = sol(a, n)

print(len(answer), *answer, sep='\n')
