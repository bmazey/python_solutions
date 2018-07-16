from challenges.interview.src.palindrome import Palindrome


def test_is_palindrome():
    assert Palindrome.is_palindrome(s='racecar')
    assert Palindrome.is_palindrome(s='civic')
    assert Palindrome.is_palindrome(s='kayak')
    assert Palindrome.is_palindrome(s='madam')


def test_is_not_palindrome():
    assert not Palindrome.is_palindrome(s='kitten')
    assert not Palindrome.is_palindrome(s='milkshake')
    assert not Palindrome.is_palindrome(s='stingray')
    assert not Palindrome.is_palindrome(s='psychic')
