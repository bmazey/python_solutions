from challenges.interview.src.password_generator import PasswordGenerator


def test_palindrome_length():
    assert len(PasswordGenerator.generate_password()) == 10


def test_palindrome_letters():
    assert PasswordGenerator.generate_password()[0].isalpha()
    assert PasswordGenerator.generate_password()[1].isalpha()
    assert PasswordGenerator.generate_password()[2].isalpha()
    assert PasswordGenerator.generate_password()[3].isalpha()
    assert PasswordGenerator.generate_password()[4].isalpha()


def test_palindrome_digits():
    assert PasswordGenerator.generate_password()[5].isdigit()
    assert PasswordGenerator.generate_password()[6].isdigit()
    assert PasswordGenerator.generate_password()[7].isdigit()
    assert PasswordGenerator.generate_password()[8].isdigit()


def test_palindrome_symbols():
    assert containsAny(PasswordGenerator.generate_password()[9], '!@#$%^&*')


def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]
