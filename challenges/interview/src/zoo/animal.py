class Animal:
    """this is our animal interface"""

    # all Animals have a name
    def __init__(self, name):
        self.name = name

    # all Animals eat
    def eat(self):
        return "nom ... nom ..."
