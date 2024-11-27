try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except (ValueError, ZeroDivisionError) as e:
    print(e)
else:
    print(f'The result is: {result}')
finally:
    print('End of the program')