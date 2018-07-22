from challenges.interview.src.password_generator import PasswordGenerator


def test_password_length():
    assert len(PasswordGenerator.generate_password()) == 10


def test_password_letters():
    assert PasswordGenerator.generate_password()[0].isalpha()
    assert PasswordGenerator.generate_password()[1].isalpha()
    assert PasswordGenerator.generate_password()[2].isalpha()
    assert PasswordGenerator.generate_password()[3].isalpha()
    assert PasswordGenerator.generate_password()[4].isalpha()


def test_password_digits():
    assert PasswordGenerator.generate_password()[5].isdigit()
    assert PasswordGenerator.generate_password()[6].isdigit()
    assert PasswordGenerator.generate_password()[7].isdigit()
    assert PasswordGenerator.generate_password()[8].isdigit()


def test_password_symbols():
    assert containsAny(PasswordGenerator.generate_password()[9], '!@#$%^&*')


def test_password_uniqueness():
    # note! there is a small chance this test may fail because of uniqueness.
    # for now, we can ignore one-of failures on this test
    password1 = PasswordGenerator.generate_password()
    password2 = PasswordGenerator.generate_password()

    assert password1 != password2


def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]
