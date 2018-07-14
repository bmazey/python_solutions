class FizzBuzz:
    """This is our FizzBuzz class"""
    def fizzbuzz(self, i):
        string = ''
        if (i % 3) == 0:
            string += 'fizz'

        if (i % 5 ) == 0:
            string += 'buzz'
        return string
