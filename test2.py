number = int(input())
i = 2
print(number, '= ', end='')
while number != 0:
    if number % i == 0:
        if number // i == 1:
            print(i)
        if number // i > 1:
            print(i, '* ', end='')
        number = number // i
    if number % i != 0:
        i = i + 1
