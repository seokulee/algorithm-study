def eua(a, b):
    c, d = 1, 0

    while b: 
        a, b, c, d = b, a % b, d, c - a//b*d
    
    return a, c


def combine(m1, m2, r1, r2):
    gcd, m1_inv = eua(m1, m2)
    d = r2 - r1
    
    if d % gcd != 0: return False

    lcm = m1 * m2 // gcd
    k = (m1_inv * d // gcd) % (m2 // gcd)
    r = (m1 * k + r1) % lcm

    return lcm, r


def sol(nums):
    prev = nums[0], nums[3]

    for mod, i in zip(nums[1:3], nums[4:]):
        v = combine(prev[0], mod, prev[1], i)
        
        if v: prev = v
        else: return -1

    return prev[1]


nums = tuple(map(int, input().split()))

print(sol(nums))
