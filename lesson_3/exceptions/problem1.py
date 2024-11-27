try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except ValueError:
    print('enter valid numbers')
except ZeroDivisionError:
    print('cannot devide by zero!')