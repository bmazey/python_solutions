
class Car(object):
    def __init__(self, wheels=4, doors=4, fuel="Unleaded Gas", color="Black"):
        self.wheels = wheels
        self.doors = doors
        self.fuel = fuel
        self.color = color

    def __str__(self):
        return "This is a {0} car with {1) wheels and {2} doors. " \
               "It runs on {3}.".format(self.color, self.wheels, self.doors, self.fuel)

