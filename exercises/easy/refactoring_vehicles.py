class Vehicle:
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels

    def info(self):
        return f"{self.make} {self.model}"
    
    
    def get_wheels(self):
        return self.wheels
    
    

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload




car = Car('Toyota', 'RAV4')
print(car.info())
print(car.get_wheels())

motorcycle = Motorcycle('Harley Davidson', 'P12')
print(motorcycle.info())
print(motorcycle.get_wheels())

truck = Truck('Ford', 'F150', '50 cubic feet')
print(truck.info())
print(truck.get_wheels())
    