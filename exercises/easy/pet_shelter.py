class Pet:
    def __init__(self, animal_type, name):
        self._animal_type = animal_type
        self._name = name
    
    @property
    def animal_type(self):
        return self._animal_type
    
    @property
    def name(self):
        return self._name
    
    def info(self):
        return f'a {self.animal_type} named {self.name}'
    

class Owner:
    def __init__(self, name):
        self._name = name
        self.pets = []
    
    @property
    def name(self):
        return self._name
    
    
    def number_of_pets(self):
        return len(self.pets)
    
    def add_pet(self, pet):
        self.pets.append(pet)

    def print_pets(self):
        for pet in self.pets:
            print(pet.info())
    

    

class Shelter:

    def __init__(self):
        self.owners = {}


    def adopt(self, owner, pet):
        owner.add_pet(pet)
        self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            if name == 'The Animal Shelter':
                print(f'{name} has the following unadopted pets:')
                owner.print_pets()
                print()
            print(f'{name} has adopted the following pets:')
            owner.print_pets()
            print()




cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')



phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')
the_animal_shelter = Owner('The Animal Shelter')


shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.adopt(the_animal_shelter, asta)
shelter.adopt(the_animal_shelter, laddie)
shelter.adopt(the_animal_shelter, fluffy)
shelter.adopt(the_animal_shelter, kat)
shelter.adopt(the_animal_shelter, ben)
shelter.adopt(the_animal_shelter, chatterbox)
shelter.adopt(the_animal_shelter, bluebell)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print((f"{the_animal_shelter.name} has "
      f"{the_animal_shelter.number_of_pets()} unadopted pets."))

    
