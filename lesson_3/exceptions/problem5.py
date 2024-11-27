class NegativeNumberError(ValueError):
    def __init__(self, message="Number can't be negative!"):
        super().__init__(message)




num = float(input('Enter a number: '))
if num < 0:
    raise NegativeNumberError
print(f"You entered {num}")