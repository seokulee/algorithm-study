def get_next_prime(n):
    if n <= 2:
        return 2
    
    elif n == 3:
        return 3
    
    while True:
        max_prime = int(n ** (1/2))

        for i in range(2, max_prime + 1):
            if n % i == 0:
                break
        else:
            return n

        n += 1

        
count = int(input())

for i in range(count):
    n = int(input())

    print(get_next_prime(n))
    