import random
import challenges.interview.src.fizzbuzz as fb

def test_fizzbuzz():
    assert fb.FizzBuzz.fizzbuzz()
    k = random.randint(1, 101)