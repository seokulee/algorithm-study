def solve_n_queens(n):
    def dfs(row, cols, diag1, diag2):
        if row == n:
            nonlocal count
            count += 1
            return
        available_positions = ((1 << n) - 1) & ~(cols | diag1 | diag2)
        while available_positions:
            position = available_positions & -available_positions
            available_positions -= position
            dfs(row + 1, cols | position, (diag1 | position) << 1, (diag2 | position) >> 1)

    count = 0
    dfs(0, 0, 0, 0)
    return count

n = int(input())
print(solve_n_queens(n))







# def add_to_set(x, y):
#     dup.update((f"x={x}", f"y={y}", f"y=x+{y - x}", f"y=-x+{y + x}"))

# def sub_from_set(x, y):
#     for s in f"x={x}", f"y={y}", f"y=x+{y - x}", f"y=-x+{y + x}":
#         dup.remove(s)

# def find_q(i, c):
#     if c == 0:
#         return 1
    
#     sum_of_case = 0
#     for i in range(i, max_index):
#         ix, iy = i%n, i//n
#         if all(s not in dup for s in (f"x={ix}", f"y={iy}", f"y=x+{iy - ix}", f"y=-x+{iy + ix}")):
#             add_to_set(ix, iy)
#             sum_of_case += find_q(i+1, c-1)
#             sub_from_set(ix, iy)

#     return sum_of_case


# n = int(input())
# max_index = n**2
# dup = set()

# print(find_q(0, n))









# def add_tile(arr, x, y, num):
#     for i in range(n):
#         arr[y][i] += num
#         arr[i][x] += num

#     b = y - x
#     lbx, lby = (0, b) if b >= 0 else (-b, 0)
#     for i in range(n - abs(b)):
#         arr[lby+i][lbx+i] += num
    
#     b = y + x
#     n2 = n - 1
#     ltx, lty = (0, b) if b < n else (b-n2, n2)
#     for i in range(-abs(b-n2) + n):
#         arr[lty-i][ltx+i] += num


# def find_q(arr, i, c):
#     if c == 0:
#         return 1
    
#     sum_of_case = 0
#     for i in range(i, max_index):
#         iy, ix = i//n, i%n
#         if not arr[iy][ix]:
#             add_tile(arr, ix, iy, 1)
#             sum_of_case += find_q(arr, i+1, c-1)
#             add_tile(arr, ix, iy, -1)

#     return sum_of_case


# n = int(input())
# max_index = n**2
# chess_board = [ [0 for _ in range(n)] for _ in range(n) ]

# num_of_case = find_q(chess_board, 0, n)
# print(num_of_case)











# def find_q_by_h_v(x, y):
#     if sum(chess_board[y][:]):
#         return True
    
#     for l in chess_board:
#         if l[x]:
#             return True

#     return False


# def find_q_by_dia(x, y):
#     b = y - x
#     lbx, lby = (0, b) if b >= 0 else (-b, 0)
#     for i in range(n - abs(b)):
#         if chess_board[lby+i][lbx+i]:
#             return True
    
#     b = y + x
#     ltx, lty = (0, b) if b < n else (b-(n-1), n-1)
#     for i in range(-abs(b-(n-1))+n):
#         if chess_board[lty-i][ltx+i]:
#             return True

#     return False


# def find_q(i, c):
#     if c == 0:
#         return 1
    
#     sum_of_case = 0
#     for i in range(i, max_index):
#         iy, ix = i//n, i%n
#         if not chess_board[iy][ix] and not find_q_by_h_v(ix, iy) and not find_q_by_dia(ix, iy):
#             chess_board[iy][ix] = True
#             sum_of_case += find_q(i+1, c-1)
#             chess_board[iy][ix] = False

#     return sum_of_case


# n = int(input())
# max_index = n**2
# chess_board = [ [False for _ in range(n)] for _ in range(n)]

# num_of_case = find_q(0, n)
# print(num_of_case)
