number1 = int(input())
number11 = 1
number2 = int(input())
number22 = 1
bit = 0
while number1 > 1:
    number11 = number11 * 10 + number1 % 2
    number1 = number1 // 2
while number2 > 1:
    number22 = number22 * 10 + number2 % 2
    number2 = number2 // 2
if number22 > number11:
    while number22 > 0:
        if number11 % 10 != number22 % 10:
            number11 = number11 // 10
            number22 = number22 // 10
            bit = bit + 1
        else:
            number11 = number11 // 10
            number22 = number22 // 10
elif number22 < number11:
    while number11 > 0:
        if number11 % 10 != number22 % 10:
            number11 = number11 // 10
            number22 = number22 // 10
            bit = bit + 1
        else:
            number11 = number11 // 10
            number22 = number22 // 10
print(bit)
