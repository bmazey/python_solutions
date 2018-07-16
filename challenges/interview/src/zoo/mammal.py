from challenges.interview.src.zoo.animal import Animal


class Mammal(Animal):
    """this 'abstract class' defines a Mammal"""
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = True
        self.vertebrate = True

    # examples ... using @property later
    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    # all mammals have specialized teeth ... they eat differently!
    # @override
    def eat(self):
        return 'munch ... munch ...'
