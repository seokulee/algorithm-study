import sys



class Heap():
    def __init__(self):
        self.dp = []
    
    def push(self, n):
        self.dp.append(n)
        child = len(self.dp) - 1

        while child and self.dp[child] > self.dp[parent := (child-1)//2]:
            self.dp[child], self.dp[parent] = self.dp[parent], self.dp[child]
            child = parent

    def pop(self):
        leng = len(self.dp)
        if not leng: return 0
        elif leng == 1: return self.dp.pop()

        ret = self.dp[0]
        self.dp[0] = self.dp.pop()
        leng -= 1
        parent = 0

        while 1:
            child1 = 2*parent + 1
            child2 = child1 + 1
            largest = parent 
            
            if child1 < leng and self.dp[largest] < self.dp[child1]: largest = child1
            if child2 < leng and self.dp[largest] < self.dp[child2]: largest = child2
            if largest == parent: break

            self.dp[parent], self.dp[largest] = self.dp[largest], self.dp[parent]
            parent = largest

        return ret


readline = sys.stdin.readline
heap = Heap()

for _ in range(int(readline())):
    n = int(readline())

    if n: heap.push(n)   
    else:sys.stdout.write(str(heap.pop()) + '\n')
