import math as m

def calc():
    while True:
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter a second number: '))
        operator = input('What operaiton would you like to do? (+, -, /, *, ^, sqrt) ')

        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '/':
            print(num1 / num2)
        elif operator == '*':
            print(num1 * num2)
        elif operator == '^':
            num = num1
            while num2 > 1:
                num *= num1
                num2 -= 1
            print(num or 'Err')
        elif operator.lower().strip() == 'sqrt':
            num1 = m.sqrt(num1)
            num2 = m.sqrt(num2)
            print(num1, num2)
        else:
            print('Not a valid operator')
            continue
calc()