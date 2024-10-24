def star(n):
    if n == 3: return ('  *  ', ' * * ', '*****')

    n //= 2
    arr = star(n)
    space = ' ' * n

    new_arr = [space + a + space for a in arr]
    new_arr += [a + ' ' +  a for a in arr]

    return new_arr

print(*star(int(input())), sep='\n')
