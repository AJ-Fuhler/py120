class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() <= other.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() >= other.name.casefold()
    

fuzzy = Cat('fuzzy')
fuzy = Cat('Fuzy')
fuzzzy = Cat('Fuzzy')

print(fuzzy > fuzy) # True
print(fuzzy >= fuzzzy) # True
print(fuzy <= fuzzy) # True
print(fuzzzy < fuzy) # False