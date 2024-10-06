for i in range(3):
    string = input()
    if string.isdecimal():
        num = int(string) + 3 - i
        break

print('Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or num)
