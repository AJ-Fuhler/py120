class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
# cat1.color

# mro for cat1.color:
# Cat, Animal, object

print([cls.__name__ for cls in Cat.mro()])