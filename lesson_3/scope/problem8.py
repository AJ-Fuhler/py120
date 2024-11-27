class Car:

    manufacturer = 'Toyota'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f'{Car.manufacturer=}')
        print(f'{self.manufacturer=}')


car = Car('Honda')
car.show_manufacturer()