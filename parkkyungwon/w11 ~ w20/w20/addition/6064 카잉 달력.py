def get_gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


def sol(lessm, greatm, lessv, greatv):
    gcd = get_gcd(greatm, lessm)

    if lessv % gcd != greatv % gcd: return -1

    max_cycle = greatm // gcd

    for i in range(max_cycle):
        year = lessv + i*lessm
        det = v if (v := year % greatm) else greatm

        if det == greatv: return year
        

ss = open(0).read().splitlines()

for M, N, x, y in (map(int, s.split()) for s in ss[1:]):
    if M < N: lessm, greatm, lessv, greatv = M, N, x, y
    else: lessm, greatm, lessv, greatv = N, M, y, x

    print(sol(lessm, greatm, lessv, greatv))
