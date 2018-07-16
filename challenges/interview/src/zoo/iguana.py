from challenges.interview.src.zoo.reptile import Reptile


class Iguana(Reptile):
    """this is our public Iguana class, which 'extends' Reptile"""
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.color = 'green'
        self.size = 3

    def get_legs(self):
        return self.legs

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    # @override test
    def eat(self):
        return "crunch ... crunch ..."
