class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string.')
        if new_name == '':
            raise ValueError('Name can not be an empty string.')
        
        self._name = new_name


donnie = Person('Donnie')
print(donnie.name) # Donnie
donnie.name = 'AJ'
print(donnie.name) # AJ
donnie.name = '' # ValueError
