import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        return re.match(r'(.*)cat(.*)', s)

    @staticmethod
    def alphanumeric_glyph(s):
        return re.match(r'[a-z]{4}[0-9]{5,7}', s)

    @staticmethod
    def avoid_nile_crocodile(s):
        return re.match(r'^((?!crocodile).)*$', s)

    @staticmethod
    def find_gold_scarab(s):
        match = re.match(r'gold(?= scarab)', s)
        if match:
            print("match detected! " + match.group())
            return match.group()
        else:
            return False

    @staticmethod
    def raid_tuts_tomb(s):
        return re.match(r'test',s, re.I)

    @staticmethod
    def steal_crystal_skull(s):
        return s.replace('skull', 'idol')
