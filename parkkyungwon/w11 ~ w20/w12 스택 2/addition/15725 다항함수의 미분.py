def sol(p):
    if 'x' not in p:
        return 0
    
    p = p.split('x')
    if p[0] == '':
        return 1
    elif p[0] == '-':
        return -1
    else:
        return int(p[0])

p = input()
print(sol(p))
