class Palindrome(object):
    """this is our palindrome class"""

    @staticmethod
    def is_palindrome(s):

        reverse = ''
        for i in range(len(s)):
            reverse += s[len(s) - 1 - i]
        if s == reverse:
            return True
        else:
            return False
