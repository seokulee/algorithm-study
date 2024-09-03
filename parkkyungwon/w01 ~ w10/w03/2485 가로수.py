import sys



def get_gcd(a, b):
    while(b):
        a, b = b, a % b
    
    return a


def get_gci(x):
    while len(x) != 1:
        ### 시간초과 발생으로, 중복 연산 제거를 위해 set을 사용
        x = {get_gcd(a, b) for a, b in zip(x[:-1], x[1:])}
        x = tuple(x)
    
    return x[0]


count = int(sys.stdin.readline())

colonnade = []
for _ in range(count):
    colonnade.append(int(sys.stdin.readline()))

intervals = [b - a for a, b in zip(colonnade[:-1], colonnade[1:])]
### 주변 interval 간의 gcd를 구함
gci = get_gci(intervals)

result = sum(intervals) // gci - len(intervals)
print(result)
