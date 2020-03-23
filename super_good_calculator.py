import math

number_1 = float(input('Enter first number: '))
operator = input('Enter operator: ')
number_2 = float(input('Enter second number: '))

if operator == '+':
    print(number_1 + number_2)
elif operator == '-':
    print(number_1 - number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == '/':
    print(number_1 / number_2)
else:
    print('Invalid operator')

x = -3.7
print(round(x))
print(abs(x))
print(math.floor(x))
print(math.ceil(x))
