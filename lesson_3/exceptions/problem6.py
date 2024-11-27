numbers = [1, 3, 6, 25, 0, 4]

def inverse(numbers):
    inversed_numbers = []
    for number in numbers:
        try:
            inversed_numbers.append(1 / number)
        except ZeroDivisionError:
            inversed_numbers.append(float('inf'))
        
    return inversed_numbers

print(inverse(numbers))