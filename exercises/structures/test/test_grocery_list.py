import pytest

from exercises.structures.src.grocery_list import GroceryList

def test_first_item():
    gl = GroceryList()
    gl.populate_list()
    assert gl.first() == 'milk'