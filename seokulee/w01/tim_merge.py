# 2751번 시간 복잡도 O(nlogn)
# merge, heap ...
# python은 Timsort를 사용함. (Insert sort, Merge sort를 결합하여 만듦)

# merge, heap, quick 중 안정적인 Merge sort 구현하기
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = r = 0
    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
            merged_arr.append(l_arr[l])
            l += 1
        else:
            merged_arr.append(r_arr[r])
            r += 1

    merged_arr += l_arr[l:]
    merged_arr += r_arr[r:]

    return merged_arr

import random
import time
import copy

arr = random.sample(range(1, 1000001), 1000000)
arr2 = copy.deepcopy(arr)

# tim sort 소요시간 측정
start = time.time()
arr.sort()
end = time.time()
print(f"Tim-Sort : {end-start:.5f}")

# merge sort 소요시간 측정
start = time.time()
merge_sort(arr2)
end = time.time()
print(f"Merge-sort : {end - start:.5f}")

# 결론 : 그냥 내장함수 쓰라잇!
