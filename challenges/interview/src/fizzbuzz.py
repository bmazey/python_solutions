class FizzBuzz(object):
    """This is our FizzBuzz class"""
    @staticmethod
    def fizzbuzz(i):
        string = ''
        if (i % 3) == 0:
            string += 'fizz'

        if (i % 5) == 0:
            string += 'buzz'
        return string
