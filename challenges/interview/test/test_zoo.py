from challenges.interview.src.zoo.panther import Panther
from challenges.interview.src.zoo.kitten import Kitten
from challenges.interview.src.zoo.iguana import Iguana


def test_panther_properties():
    panther = Panther('Bagheera')

    assert panther.is_verterbrate()
    assert panther.is_warm_blooded()

    # ... to be continued ...


def test_kitten_properties():
    kitten = Kitten('Maru')

    assert kitten.legs == 4

    # ... maybe add methods? ...


def test_iguana_properties():
    iguana = Iguana('Alphys')

    assert iguana.is_warm_blooded() == False
    assert iguana.get_color() == 'green'.casefold()

    # ... add more ...
