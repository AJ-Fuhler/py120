students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'
    

print(get_age('John'))
print(get_age('Joe'))
print(get_age('Jane'))