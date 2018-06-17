
class Car(object):
    def __init__(self, wheels=4, doors=4, fuel="Unleaded Gas", color="Black"):
        self.wheels = wheels
        self.doors = doors
        self.fuel = fuel
        self.color = color

    def __str__(self):
        return "This is a {} car with {} wheels and {} doors. " \
               "It runs on {}.".format(self.color, self.wheels, self.doors, self.fuel)

