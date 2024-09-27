import bisect



def sol(heights, area):
    def get_cost(h):
        i = bisect.bisect_left(heights, h+1) - 1

        rect =  h * (LI - i)
        above = cum_sum[-1] - cum_sum[i] - rect
        under = h * area - cum_sum[i] - rect

        return 2*above + under
    
    def compare(a, b):
        if a[0] > b[0] or (a[0] == b[0] and a[1] < b[1]): 
            a[0], a[1] = b[0], b[1]
            return True

        return False

    L = len(heights)
    LI = L - 1
    cum_sum = heights.copy()
    for i in range(LI): 
        cum_sum[i+1] += cum_sum[i]

    end_h = (cum_sum[-1] + B) // area
    start_h = heights[0]

    sep = area // 3
    mid_h = (cum_sum[sep] + cum_sum[-1]) // (area + sep + 1)

    g_min = [float('inf')] * 2

    for ite in (range(mid_h-1, start_h-1, -1), range(mid_h, end_h+1)):
        l_min = [float('inf')] * 2

        for i in ite:
            if not compare(l_min, (get_cost(i), i)): break
        
        compare(g_min, l_min)

    return g_min


ss = open(0).read().splitlines()
N, M, B = map(int, ss[0].split())
heights = []

for s in ss[1:]:
    heights.extend(map(int, s.split()))

heights.sort()

print(*sol(heights, N * M))
