from challenges.interview.src.palindrome import Palindrome

def test_palindrome():
    assert Palindrome.is_palindrome(s='racecar') == True
    assert Palindrome.is_palindrome(s='civic') == True
    assert Palindrome.is_palindrome(s='kayak') == True
    assert Palindrome.is_palindrome(s='madam') == True

    assert Palindrome.is_palindrome(s='kitten') == False
    assert Palindrome.is_palindrome(s='milkshake') == False
    assert Palindrome.is_palindrome(s='stingray') == False
    assert Palindrome.is_palindrome(s='psychic') == False
