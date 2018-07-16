from exercises.structures.src.treasure_map import TreasureMap

tm = TreasureMap()
tm.populate_map()


def test_beach_key():
    assert tm.map['beach'] == 'sandy shore'.casefold()


def test_coast_key():
    assert tm.map['coast'] == 'ocean reef'.casefold()


def test_volcano_key():
    assert tm.map['volcano'] == 'hot lava'.casefold()


def test_x_key():
    assert tm.map['x'] == 'marks the spot'.casefold()

