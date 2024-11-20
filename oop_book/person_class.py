class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"
    
    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError("Name must be alphabetic.")

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name.title()
        self._last_name = last_name.title()
    


friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.