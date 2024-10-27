import math



def sudoku(tile):
    def dfs(i, h, v, s):
        if i == target_len:
            return True
        
        x, y = target_coor[i]        
        for_s = (y//3 * 3 + x//3) * 9
        avail_digit = ((1 << 9) - 1) & ~(h >> (y * 9) | v >> (x * 9) | s >> for_s)
        while avail_digit:
            digit = avail_digit & -avail_digit
            avail_digit -= digit

            if dfs(i + 1, h | (digit << (9 * y)), v | (digit << (9 * x)), s | digit << for_s):
                tile[y][x] = round(math.log2(digit)) + 1
                return True
                
        return False

    h, v, s = 0, 0, 0
    target_coor = []
    for y in range(9):
        for x in range(9):
            if tile[y][x]:
                bit = 1 << tile[y][x] - 1

                h |= bit << 9 * y
                v |= bit << 9 * x
                s |= bit << (9 * (y//3 * 3 + x//3))

            else:
                target_coor.append((x, y))
    
    target_len = len(target_coor)

    # print(*list(map(lambda x: format(x, '#b'), (h, v, s))), sep='\n')
    # return

    dfs(0, h, v, s)


tile = [list(map(int, input().split())) for _ in range(9)]

sudoku(tile)

print('\n' + '\n'.join(' '.join(map(str, t)) for t in tile))
