class Cat:
    
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello! My name is {self.name}!")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()