from exercises.patterns.builder.car import Car
from exercises.patterns.builder.builder import Builder

class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value

    def set_doors(self, value):
        self.car.doors = value

    def set_fuel(self, value):
        self.car.fuel = value

    def set_color(self, value):
        self.car.color = value

    def get_result(self):
        return self.car

