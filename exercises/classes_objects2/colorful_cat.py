class Cat:
    COLOR = 'purple'

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {Cat.COLOR} cat!")


sophie = Cat('Sophie')
sophie.greet()