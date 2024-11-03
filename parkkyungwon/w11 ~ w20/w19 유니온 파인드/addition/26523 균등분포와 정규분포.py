read = open(0)

for _ in range(100):
    count = 0

    for _ in range(5000):
        # 0과 0.1의 값만 카운팅
        if read.readline()[2] == '0': count += 1

    # count의 기대값은 균등분포이면 500, 정규분포면 264. 그래서 절반인 382를 기준으로 나눔
    print("A" if count > 382 else "B")
