import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        return

    @staticmethod
    def alphanumeric_glyph(s):
        return re.match(r'[a-z]{4}[0-9]{5}', s)
