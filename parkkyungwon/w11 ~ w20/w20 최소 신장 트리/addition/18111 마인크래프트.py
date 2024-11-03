import bisect


def upward_condition(heights, i, j):
    return False if i == L else heights[i + 1] <= j

def downward_condition(heights, i, j):
    return heights[i] > j

def compare(a, b):
        if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]): a[0], a[1] = b[0], b[1]; return False
        return True


def sol(heights, area):
    def get_cost(s, e, step, condition):
        min_v = [float('inf')] * 2
        i = bisect.bisect_left(heights, s+1) - 1

        for j in range(s, e, step):
            while condition(heights, i, j):
                i += step
                
            cost = 2*cum_sum[-1] - 3*(cum_sum[i] + j*(L - i)) + j*area 
            
            if compare(min_v, (cost, j)): break

        return min_v

    cum_sum = heights.copy()
    for i in range(L): 
        cum_sum[i+1] += cum_sum[i]

    end_h = (cum_sum[-1] + B) // area
    start_h = heights[0]

    sep = area // 3
    mid_h = (cum_sum[sep] + cum_sum[-1]) // (area + sep + 1)

    a = get_cost(mid_h-1, start_h-1, -1, downward_condition)
    b = get_cost(mid_h, end_h+1, 1, upward_condition)
    compare(a, b)

    return a


ss = open(0).read().splitlines()
N, M, B = map(int, ss[0].split())
heights = []

for s in ss[1:]:
    heights.extend(map(int, s.split()))

heights.sort()

L = len(heights) - 1

print(*sol(heights, N * M))
