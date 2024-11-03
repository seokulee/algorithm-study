import sys



def sol(arr):
    rows, cols, sqrs = [[0] * 9 for _ in range(3)]
    bits = [1 << i for i in range(1, 10)]
    full_bit = (1 << 10) - 2

    for y in range(9):
        for x in range(9):
            if not arr[y][x]: continue

            bit = 1 << arr[y][x]

            rows[y] |= bit ; cols[x] |= bit ; sqrs[(y//3 * 3) + x//3] |= bit

    def backtrack(y, x):
        if y == 9: return True
        if x == 8: dy, dx = y+1, 0 
        else: dy, dx = y, x+1

        if arr[y][x]:
            if backtrack(dy, dx): return True
            return

        sqrsi = (y//3 * 3) + x//3
        cum_bit = rows[y] | cols[x] | sqrs[sqrsi]

        if cum_bit == full_bit : return

        for i, bit in enumerate(bits, 1):
            if cum_bit & bit: continue

            rows[y] |= bit ; cols[x] |= bit ; sqrs[sqrsi] |= bit

            if backtrack(dy, dx): 
                arr[y][x] = i
                return True
            
            rows[y] ^= bit ; cols[x] ^= bit ; sqrs[sqrsi] ^= bit
    
    backtrack(0, 0)


arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]

sol(arr)

for a in arr:
    sys.stdout.write(''.join(map(str, a)) + '\n')
