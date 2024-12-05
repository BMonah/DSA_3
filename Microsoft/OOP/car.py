class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return 'My car is driving'

    def stop(self):
        print('my car has stopped')
