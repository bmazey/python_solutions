from challenges.interview.src.zoo.mammal import Mammal

class Panther(Mammal):
    """this is our Panther class which 'extends' Mammal"""
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.color = 'black'
        self.size = 5

    def call(self):
        return "ROAR!"
