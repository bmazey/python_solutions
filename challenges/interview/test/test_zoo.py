from challenges.interview.src.zoo.panther import Panther
from challenges.interview.src.zoo.kitten import Kitten
from challenges.interview.src.zoo.iguana import Iguana


def test_panther_properties():
    panther = Panther('Bagheera')

    assert panther.size == 5
    assert panther.legs == 4
    assert panther.is_vertebrate()
    assert panther.is_warm_blooded()
    assert 'black' == panther.color.casefold()
    assert "ROAR!" == panther.call()
    assert "munch ... munch ..." == panther.eat().casefold()


def test_kitten_properties():
    kitten = Kitten('Maru')

    assert kitten.size == 1
    assert kitten.legs == 4
    assert kitten.vertebrate
    assert kitten.warm_blooded
    assert 'orange' == kitten.color.casefold()
    assert "meow ... meow ..." == kitten.call().casefold()
    assert "munch ... munch ..." == kitten.eat().casefold()


def test_iguana_properties():
    iguana = Iguana('Alphys')

    assert iguana.get_size() == 3
    assert iguana.get_legs() == 4
    assert not iguana.is_warm_blooded()
    assert iguana.get_color() == 'green'.casefold()
    assert "crunch ... crunch ..." == iguana.eat().casefold()
