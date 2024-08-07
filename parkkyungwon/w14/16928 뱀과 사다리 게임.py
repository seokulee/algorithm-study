import sys



def sol(data):
    # 주사위를 굴려서 발생할 수 있는 경우를 전부 저장한다.
    table = tuple(set() for _ in range(101))
    for i in range(1, 95):
        table[i].update(range(i+1, i+7))
    for i in range(95, 100):
        table[i].update(range(i+1, 101))

    # 사다리나 뱀의 경우는 예를 들어서 12 -> 98로 이동할 수 있다면, 
    # 주사위를 굴려서 12가 나올 수 있는 인덱스의 테이블에 12를 제거하고 98를 추가한다 
    for a, b in data:
        mini = a - 6 if a > 6 else 1
        for i in range(mini, a):
            table[i].add(b)
            table[i].remove(a)

    # bfs
    hist = set()
    queue = [1, -1]
    count = 0
    for a in queue:
        if a == -1:
            count += 1
            queue.append(-1)
            continue
        
        elif a == 100:
            break

        for b in table[a]:
            if b in hist:
                continue

            queue.append(b)
            hist.add(b)
    
    return count
            
    
readline = sys.stdin.readline
N, M = map(int, readline().split())
data = (map(int, readline().split()) for _ in range(N + M))

print(sol(data))
