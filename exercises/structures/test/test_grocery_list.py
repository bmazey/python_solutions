from exercises.structures.src.grocery_list import GroceryList


gl = GroceryList()
gl.populate_list()


def test_first_item():
    assert gl.first() == 'milk'


def test_number_of_items():
    assert len(gl.items) == 5


def test_second_item():
    assert gl.items[1] == 'eggs'


def test_third_item():
    assert gl.items[2] == 'seltzer'


def test_third_item_equals_fifth_item():
    assert gl.items[2] == gl.items[4]


def test_fourth_item():
    assert gl.items[3] == 'honey'

