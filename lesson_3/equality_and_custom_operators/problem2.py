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
    

fuzzy = Cat('fuzzy')
fuzy = Cat('Fuzzy')
fuzzzy = Cat('fuzzzy')

print(fuzzy == fuzy)
print(fuzzy != fuzy)
print(fuzzy == fuzzzy)
print(fuzzy != fuzzzy)