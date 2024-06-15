import sys



def find(arr):
    s = []
    m = 0
    i = 0

    while i < len(arr):
        if not s or arr[s[-1]] <= arr[i]:
            s.append(i)
            i += 1
        else:
            top_s = s.pop()
            area = (arr[top_s] * ((i - s[-1] - 1) if s else i))
            m = max(m, area)

    while s:
        top_s = s.pop()
        area = (arr[top_s] * ((i - s[-1] - 1) if s else i))
        m = max(m, area)

    return m 


while True:
    arr = tuple(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break

    sys.stdout.write(str(find(arr[1:])) + '\n')
