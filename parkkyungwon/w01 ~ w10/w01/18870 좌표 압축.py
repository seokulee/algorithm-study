count = int(input())

coordinates = list(map(int, input().split()))

v_to_i_list = sorted(list(set(coordinates)))

v_to_i = {v: i for i, v in enumerate(v_to_i_list)}

for item in coordinates:
    print(v_to_i[item], end=' ')
    