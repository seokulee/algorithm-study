def find_sqs(n):
    max_dep = 4
    
    def f(n, dep):
        nonlocal max_dep

        if dep + 1 == max_dep: 
            if n == int(n**0.5)**2: 
                max_dep = dep
                return True

            return False
            
        for i in range(int(n ** 0.5), 0, -1):
            n2 = n - i**2

            if not n2:
                max_dep = dep
                return True

            if f(n2, dep+1): return False
        
    f(n, 1)
    
    return max_dep


N = int(input())

print(find_sqs(N))
