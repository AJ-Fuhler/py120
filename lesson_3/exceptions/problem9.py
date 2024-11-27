numbers = [1, 2, 3, 4, 5]

def fetch_sixth_element_lbyl(numbers):
    if len(numbers) > 5:
        return numbers[5]
    
    return None

def fetch_sixth_element_afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None
    
