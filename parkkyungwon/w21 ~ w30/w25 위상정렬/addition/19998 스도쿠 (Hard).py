import sys



class Node:
    def __init__(self, col=None, name=None):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.col = col
        self.name = name
        # header에서만 사용됨
        self.size = 0
    
    def append_h(self, node):
        last = self.left

        last.right = node
        self.left = node
        node.left = last
        node.right = self

    def append_v(self, node):
        last = self.up

        last.down = node
        self.up = node
        node.up = last
        node.down = self

        self.size += 1

    def cover(self):
        self.right.left = self.left
        self.left.right = self.right

        i = self.down
        while i is not self:
            j = i.right

            while j is not i:
                j.down.up = j.up
                j.up.down = j.down
                j.col.size -= 1

                j = j.right

            i = i.down

    def uncover(self):
        self.right.left = self
        self.left.right = self

        i = self.up
        while i is not self:
            j = i.left

            while j is not i:
                j.down.up = j
                j.up.down = j
                j.col.size += 1

                j = j.left

            i = i.up


class Sudoku():
    def __init__(self, arr):
        self.root = Node(name='root')
        self.arr = arr
        non_sign, row_sign, col_sign, sq_sign = 0, 1, 2, 3

        # 열 헤더 생성
        self.col_headers = {(non_sign, y, x): Node(name=(non_sign, y, x)) for y in range(9) for x in range(9)}
        for i in (row_sign, col_sign, sq_sign):
            for j in range(9):
                for v in range(1, 10):
                    self.col_headers[(i, j, v)] = Node(name=(i, j, v))

        # 열 헤더 연결
        for key in self.col_headers: self.root.append_h(self.col_headers[key])

        # 스도쿠 노드 생성
        for y in range(9):
            for x in range(9):
                for v in range(1, 10):
                    first = None

                    for col_i in ((non_sign, y, x), (row_sign, y, v), (col_sign, x, v), (sq_sign, y // 3 * 3 + x // 3, v)):
                        col = self.col_headers[col_i]
                        node = Node(col, (y, x, v))
                     
                        if first: first.append_h(node)
                        else: first = node
                        col.append_v(node)
        
        # 이미 존재하는 곳은 제거
        for y in range(9):
            for x in range(9):
                if not (v := self.arr[y][x]): continue
                
                for col_i in ((non_sign, y, x), (row_sign, y, v), (col_sign, x, v), (sq_sign, y // 3 * 3 + x // 3, v)):
                    self.col_headers[col_i].cover()


    def smallest_col(self):
        min_size = float('inf')
        col = self.root.right

        while col is not self.root:
            if col.size < min_size:
                min_size = col.size
                min_col = col

                if not min_size: break

            col = col.right
        
        return min_size, min_col

    def search(self):
        # 헤더가 비어있으면 성공
        if self.root.right is self.root: return True
        
        # 헤더중 크기가 0이 있으면 실패
        size, col = self.smallest_col()

        if not size: return
        
        col.cover()
        
        node = col.down
        while node is not col:
            i = node.right

            while i is not node:
                i.col.cover()
                i = i.right

            if self.search():
                y, x, v = node.name
                self.arr[y][x] = v
                return True

            i = node.left
            while i is not node:
                i.col.uncover()
                i = i.left

            node = node.down
        
        col.uncover()


arr = sys.stdin.read().splitlines()

for i in range(9): 
    arr[i] = list(map(int, arr[i].split()))

Sudoku(arr).search()

for a in arr:
    sys.stdout.write(' '.join(map(str, a)) + '\n')
