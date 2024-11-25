class Person:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'.strip()
    
    @name.setter
    def name(self, name):
        parts = name.split()
        self._first_name = parts[0]
        self._last_name = ''
        if len(parts) > 1:
            self._last_name = parts[1]
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        self._first_name = name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        return self.name == other.name
    
    def __str__(self):
        return self.name
    


bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
# without __str__ override:
# The person's name is: <__main__.Person object at 0x7f4ce0162cf0>
# with __str__ override:
# The person's name is: Robert Smith

