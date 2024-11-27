class Student:

    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name


aj = Student('AJ')
donnie = Student('Donnie')

print(aj.name)
print(aj.__class__.school_name)
print(donnie.name)
print(donnie.__class__.school_name)