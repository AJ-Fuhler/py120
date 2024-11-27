class Dog:
    def __init__(self, breed):
        self.breed = breed


golden = Dog('Golden Retriever')
poodle = Dog('Poodle')

print(golden.breed)
print(poodle.breed)