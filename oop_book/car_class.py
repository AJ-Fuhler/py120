
class Car:

    def __init__(self, model, model_year, color):
        self.speed = 0
        self._model = model
        self._color = color
        self._model_year = model_year
        
        
    def start_engine(self):
        print('PRRRRRRR, the engine started...')
    
    def accelerate(self, number):
        self.speed += number
        print(f"VROOM!! You accelerated {number} MPH.")
    
    def get_speed(self):
        print(f'Your speed is {self.speed} MPH')
    
    def brake(self, number):
        self.speed -= number
        print(f"You decelerated {number} MPH.")
    
    
    def stop_engine(self):
        if self.speed != 0:
            print("Can't stop engine, you're not standing still!")
        else:
            print('Your engine is now turned off.')

    @staticmethod
    def gas_mileage(gallons, miles):
        mileage = miles / gallons
        print(f"{mileage} miles per gallon")
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        print(f"Changing colors from {self._color} to {new_color}.")
        self._color = new_color

    @property
    def year(self):
        return self._model_year
    
    @property
    def model(self):
        return self._model
    
    def spray_paint(self, color):
        self._color = color
        print(f"Your {color} paint job looks great!")

        
        

margery = Car('RAV4', 2008, 'grey')

margery.start_engine()
margery.accelerate(10)
margery.accelerate(20)
margery.get_speed()
margery.brake(28)
margery.get_speed()
margery.stop_engine()
margery.brake(2)
margery.stop_engine()
print(margery.color)
margery.color = 'blue'
print(margery.color)
print(margery.model)
print(margery.year)
margery.spray_paint('Red')
print(margery.color)
Car.gas_mileage(13, 351)

    