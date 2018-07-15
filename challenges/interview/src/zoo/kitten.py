from challenges.interview.src.zoo.mammal import Mammal

class Kitten(Mammal):
    """this is our Tiger class which 'extends' Mammal"""
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4
        self.color = 'orange'
        self.size = 1

    def call(self):
        return "meow ... meow ..."
