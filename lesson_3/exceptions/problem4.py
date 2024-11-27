num = float(input('Enter a number: '))
if num < 0:
    raise ValueError('Number must be positive!')
print(f"You entered {num}")