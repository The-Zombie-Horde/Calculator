print('Welcome to a calculator! This calculator will be a basic calculator until I update it')


def add(num, num1):
    num2 = num + num1
    return num2


def subtract(num, num1):
    num2 = num - num1
    return num2


def multiply(num, num1):
    num2 = num * num1
    return num2


def divide(num, num1):
    num2 = num / num1
    return num2


def divide_rounded(num, num1):
    num2 = num // num1
    return num2


def modulus(num, num1):
    num2 = num % num1
    return num2


def square(num, num1):
    num2 = num ** num1
    return num2


playing = True
while playing:
    num = int(input('Give me a number, any number!     '))
    num1 = int(input('Give me another number, any number!     '))
    thought = input('Would you like to add, subtract, multiply, divide, '
                    'divide rounded, remainder of two divided numbers, and finally square')
    if thought.lower == 'add' or thought == '+':
        num2 = add(num, num1)
    elif thought.lower == 'subtract' or thought == '-':
        num2 = subtract(num, num1)
    elif thought.lower == 'multiply' or thought == '*':
        num2 = multiply(num, num1)
    elif thought.lower == 'divide' or thought == '/':
        num2 = divide(num, num1)
    elif thought.lower == 'divide rounded' or thought == '//':
        num2 = divide_rounded(num, num1)
    elif thought.lower == 'remainder' or thought == '%':
        num2 = modulus(num, num1)
    elif thought.lower == 'square' or thought == '^2' or thought == '^' or thought == '2':
        num2 = square(num, num1)
    print('Your answer is: {}'.format(num2))
    playing = input('Do you have more numbers to calculate? [Y/n]')
    if playing.lower != 'n':
        continue
    else:
        playing = False
