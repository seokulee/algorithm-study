target = 'IO' * int(input()) + 'I'
input()
S = input()

i, count = 0, 0
L = len(target)

while (i := S.find(target, i)) != -1:
    leng = 1
    i += L

    while S[i:i+2] == 'OI':
        leng += 1
        i += 2
    
    count += leng

print(count)
