from collections import defaultdict



### a와 b의 소수를 구해서 prime_union 저장
def get_primes(num: int) -> defaultdict:
    primes = defaultdict(lambda: 0)

    max_of_prime = round(num ** (1/2))
    for i in range(2, max_of_prime + 1):
        while True:
            if num % i == 0:
                primes[i] += 1
                num = num // i
            else:
                break
    primes[num] += 1
    
    return primes


def get_common_primes(a: defaultdict, b: defaultdict):
    primes = a.copy()

    for key in b.keys():
        if primes[key] < b[key]:
            primes[key] = b[key]
    
    return primes
    

count = int(input())

for _ in range(count):
    a, b = map(int, input().split())
    
    a_prime, b_prime = get_primes(a), get_primes(b)
    common_primes = get_common_primes(a_prime, b_prime)

    least_common_multiple = 1
    for key in common_primes.keys():
        least_common_multiple *= key ** common_primes[key]

    print(least_common_multiple)
