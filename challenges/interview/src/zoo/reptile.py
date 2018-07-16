from challenges.interview.src.zoo.animal import Animal


class Reptile(Animal):
    """this is our Reptile class"""
    def __init__(self, name):
        super().__init__(name)
        self.warm_blooded = False
        self.vertebrate = True

    def is_warm_blooded(self):
        return self.warm_blooded

    def is_vertebrate(self):
        return self.vertebrate

    # reptiles make different noises when eating ...
    # @override
    def eat(self):
        return "chomp ... chomp ..."
